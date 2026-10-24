#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime
import os
from pathlib import Path

import pelican.themes.webosbrew
from pelican.plugins import webassets
from webassets.cache import MemoryCache

import repogen
from repogen.siteurl import siteurl

AUTHOR = 'Native-Webos'
SITENAME = 'Native-Webos Apps Repository'
SITEURL = siteurl() if os.environ.get('CI') else ''
PACKAGES = {}

THEME = 'webosbrew'
theme_dir = Path(__file__, '..', 'theme').resolve()
THEME_STATIC_PATHS = [pelican.themes.webosbrew.static_dir(), theme_dir.joinpath('static')]
WEBASSETS_SOURCE_PATHS = [theme_dir.joinpath('styles'), pelican.themes.webosbrew.scss_dir()]
THEME_TEMPLATES_OVERRIDES = ['./theme/templates']

PLUGINS = [webassets, repogen]

WEBASSETS_CONFIG = [
    ("CACHE", MemoryCache(1024)),
    ("PYSCSS_LOAD_PATHS", [pelican.themes.webosbrew.scss_dir()]),
]

PATH = 'content'

STATIC_PATHS = ['extra/favicon.ico', 'extra/llms.txt', 'schemas', 'apps/icons']
# App pages come from ../packages through the repogen reader. content/apps only
# holds generated icons, so it is not a page path.
PAGE_PATHS = ['pages', '../packages']

# The repo has no articles, so Pelican's article-driven templates would only emit
# empty tags/categories/authors/archives pages for crawlers to index. The plugin
# writes index.html itself.
DIRECT_TEMPLATES = []

EXTRA_PATH_METADATA = {
    'apps/icons': {'path': 'apps/icons/'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/llms.txt': {'path': 'llms.txt'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'permalink': True,
        },
    },
    'output_format': 'html5',
}

TIMEZONE = 'Australia/Hobart'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Home/logo link target and top-nav items, consumed by the theme navbar.
HOME_URL = f'{SITEURL}/'

# Directory pages keep the trailing slash. GitHub Pages 301-redirects the
# slashless form, so linking it directly saves a round trip.
MENUITEMS = (
    ('Apps', f'{SITEURL}/apps/'),
    ('Add repository', f'{SITEURL}/install'),
    ('Submit an app', f'{SITEURL}/submit'),
    ('Develop', 'https://github.com/Native-Webos/webos-native-app-kit'),
)

LINKS = (
    ('GitHub Organization', 'https://github.com/Native-Webos/'),
    ('Upstream repository', 'https://github.com/webosbrew/apps-repo'),
)

# Footer columns, consumed by the theme footer.
FOOTER_SECTIONS = [
    {'title': 'Guides', 'links': [
        {'text': 'Rooting', 'href': 'https://www.webosbrew.org/rooting'},
        {'text': 'Dev Mode', 'href': 'https://www.webosbrew.org/devmode'},
    ]},
    {'title': 'Resources', 'links': [
        {'text': 'Native App Kit', 'href': 'https://github.com/Native-Webos/webos-native-app-kit'},
        {'text': 'Submit an App', 'href': f'{SITEURL}/submit'},
    ]},
    {'title': 'Links', 'links': [
        {'text': 'Native-Webos', 'href': 'https://github.com/Native-Webos/', 'icon': 'bi-github'},
        {'text': 'OpenLGTV', 'href': 'https://github.com/OpenLGTV', 'icon': 'bi-github'},
        {'text': 'Discord', 'href': 'https://discord.gg/xWqRVEm', 'icon': 'bi-discord'},
    ]},
]

INDEX_APP_CATEGORIES = [
    ('multimedia', 'Multimedia'),
    ('game', 'Games'),
    ('amblight', 'Ambient Light'),
    ('screensaver', 'Screensavers'),
    ('launcher', 'Launchers'),
    ('utility', 'Utilities'),
]

# App IDs featured on the homepage, in display order. The blurb for each is
# taken from the package's manifest (appDescription).
FEATURED_APPS = []

# Following packages will have their IPKs downloaded and hosted on the site
HOST_PACKAGES: set[str] = set()

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

COPYRIGHT_YEAR = datetime.date.today().year
