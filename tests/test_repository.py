import json
import tempfile
import unittest
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from repogen import apidata, validators
from repogen.siteurl import siteurl
from repogen.policy import require_native_type
from repogen.pkg_info import from_package_info


class RepositoryTests(unittest.TestCase):
    def test_native_policy_rejects_web_and_missing_type(self):
        require_native_type({'type': 'native'}, 'test')
        for app_type in ('web', 'stub', 'qml', None):
            with self.subTest(app_type=app_type), self.assertRaisesRegex(ValueError, 'only native'):
                require_native_type({'type': app_type}, 'test')

    def test_registration_rejects_web_manifest(self):
        registration = dict(title='Fixture', iconUri='https://example.org/icon.png',
                            manifestUrl='https://example.org/manifest.json', category='utility',
                            pool='main', description='Test')
        with patch('repogen.pkg_info.obtain_manifest', return_value=({'type': 'web'}, datetime.now())):
            with self.assertRaisesRegex(ValueError, 'only native'):
                from_package_info('org.test.fixture', registration)

    def test_manifest_schema_rejects_web_app(self):
        manifest = dict(id='org.test.fixture', version='1.0.0', type='web', title='Fixture',
                        iconUri='https://example.org/icon.png', ipkUrl='https://example.org/app.ipk',
                        ipkHash={'sha256': '0' * 64})
        validator = validators.for_schema('api/PackageManifest.json')
        with self.assertRaises(validators.SchemaValidationError):
            validators.validate(validator, manifest)
        manifest['type'] = 'native'
        validators.validate(validator, manifest)

    def test_empty_catalog(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            apidata.generate([], root)
            for name in ('apps.json', 'apps/1.json'):
                data = json.loads((root / name).read_text())
                validators.validate(validators.for_schema('api/PackagesPage.json'), data)
                self.assertEqual(data['packages'], [])
                self.assertEqual(data['paging']['maxPage'], 1)

    def test_all_apps_present_without_client_pagination(self):
        # Synthetic records exist only in this test, never in the public catalog.
        with tempfile.TemporaryDirectory() as directory, patch.dict('os.environ', {}, clear=True):
            packages = []
            for i in range(51):
                identity = f'org.test.fixture{i}'
                manifest = dict(id=identity, version='1.0.0', type='native', title='Fixture',
                                iconUri='https://example.org/icon.png', ipkUrl='https://example.org/app.ipk',
                                ipkHash={'sha256': '0' * 64})
                packages.append(dict(id=identity, title='Fixture', iconUri=manifest['iconUri'],
                                     manifest=manifest, manifestUrl='https://example.org/manifest.json',
                                     description='Test'))
            root = Path(directory)
            apidata.generate(packages, root)
            data = json.loads((root / 'apps.json').read_text())
            validators.validate(validators.for_schema('api/PackagesPage.json'), data)
            self.assertEqual(len(data['packages']), 51)
            self.assertEqual(data['paging']['maxPage'], 1)
            self.assertTrue((root / 'apps/2.json').is_file())

    def test_local_manifest_keeps_pages_project_prefix(self):
        with tempfile.TemporaryDirectory() as directory:
            package = {'id': 'org.test.fixture', 'manifestUrl': 'file:///tmp/manifest.json',
                       'manifest': {'version': '1.0.0'}}
            apidata.fix_manifest_url(package, Path(directory))
            self.assertEqual(package['manifestUrl'], siteurl() +
                             '/api/apps/org.test.fixture/manifests/1.0.0.json')

    def test_missing_packages_rejected(self):
        with self.assertRaises(validators.SchemaValidationError):
            validators.validate(validators.for_schema('api/PackagesPage.json'), {})


if __name__ == '__main__':
    unittest.main()
