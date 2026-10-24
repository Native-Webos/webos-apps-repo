import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from repogen import apidata, validators
from repogen.siteurl import siteurl


class RepositoryTests(unittest.TestCase):
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
                manifest = dict(id=identity, version='1.0.0', type='web', title='Fixture',
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
