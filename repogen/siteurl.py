import os


def siteurl() -> str:
    return os.environ.get('REPO_SITE_URL', 'https://native-webos.github.io/webos-apps-repo').rstrip('/')
