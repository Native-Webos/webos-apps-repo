"""Check generated feeds, package counts and project-relative HTML asset links."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from repogen import validators
from repogen.siteurl import siteurl
from repogen.policy import require_native_type


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        self.urls.extend(value for key, value in attrs if key in ('href', 'src') and value)


def verify(output=Path('output')):
    base = siteurl()
    registrations = sorted(Path('packages').glob('*.yml'))
    registered_ids = {path.stem for path in registrations}
    ids = []
    for feed in (output / 'api/apps.json', output / 'api/non-free/apps.json'):
        data = json.loads(feed.read_text())
        validators.validate(validators.for_schema('api/PackagesPage.json'), data)
        for package in data['packages']:
            require_native_type(package['manifest'], 'Generated manifest')
            ids.append(package['id'])
            assert package['id'] == package['manifest']['id'], 'Manifest ID mismatch'
            assert len(package['manifest']['ipkHash']['sha256']) == 64, 'Invalid SHA-256'
            for key in ('iconUri',):
                assert package[key].startswith(('https://', 'data:')), 'Icon must be absolute'
        assert data['paging']['count'] == len(data['packages'])
        assert data['paging']['maxPage'] == 1, 'Homebrew feed must contain every package'
    assert len(ids) == len(set(ids)), 'Duplicate IDs across pools'
    assert set(ids) == registered_ids, 'Build dropped a registered application'
    assert not (output / 'CNAME').exists(), 'Inherited custom domain must not be published'
    origin = urlparse(base)
    prefix = origin.path.rstrip('/') + '/'
    for page in output.rglob('*.html'):
        parser = Links()
        parser.feed(page.read_text())
        page_url = base + '/' + page.relative_to(output).as_posix()
        for link in parser.urls:
            target = urlparse(urljoin(page_url, link))
            if target.netloc != origin.netloc or target.scheme not in ('http', 'https'):
                continue
            assert target.path.startswith(prefix), f'Link escapes project path: {link}'
            relative = unquote(target.path[len(prefix):])
            path = output / relative
            assert path.is_file() or (path / 'index.html').is_file() or path.with_suffix('.html').is_file(), \
                f'Missing local link from {page}: {link}'
    for required in ('index.html', 'apps/index.html', 'install.html', 'submit.html'):
        assert (output / required).is_file(), f'Missing {required}'
    print(f'Verified both feeds, {len(ids)} applications and generated HTML links.')


if __name__ == '__main__':
    verify()
