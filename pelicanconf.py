#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris and Jaimie Krycho'
SITENAME = 'Sap.py'
SITEURL = ''

PATH = 'content'
THEME_STATIC_DIR = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Directories to copy without modification
STATIC_PATHS = ['images', 'root']
# Redirect `root` files to the root of the output.
EXTRA_PATH_METADATA = {'root/CNAME': {'path': 'CNAME'},
                       'root/favicon.ico': {'path': 'favicon.ico'},
                       'root/favicon.png': {'path': 'favicon.png'},
                       'root/robots.txt': {'path': 'robots.txt'},
                       'root/.nojekyll': {'path': '.nojekyll'}}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugin (mostly just Pandoc!) configuration
PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['pandoc_reader']
PANDOC_ARGS = ['--smart',  # use smart typography
               '--no-highlight',  # use highlight.js instead
               '-t', 'html5',  # use HTML and its corresponding attributes
               '--section-divs',  # wrap heading-blocks with <section>
               '--filter', 'pandoc-citeproc']

# ----- Podcasting theme settings ----- #
THEME = 'podcasting-theme'

# Configure the header.
HEADER_LOGO_IMG = '/images/pythons.svg'  # path to header logo image
HEADER_USE_LOGO_ONLY = False  # Don't use header text, just use the logo alone
# Path from the root to a square (minimum 128⨉128px) version of the logo
NAV_LOGO_IMG = HEADER_LOGO_IMG
SUBTITLE = "Who says programming can't be romantic?"
