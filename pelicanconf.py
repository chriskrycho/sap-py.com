#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris and Jaimie Krycho'
SITENAME = 'sap.py'
SITEURL = ''

PATH = 'content'
THEME_STATIC_DIR = ''

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = "%B %d, %Y"
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
                       'root/sap-py.xml': {'path': 'feed.xml'},
                       'root/favicon.png': {'path': 'favicon.png'},
                       'root/robots.txt': {'path': 'robots.txt'},
                       'root/.nojekyll': {'path': '.nojekyll'}}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Plugin (mostly just Pandoc!) configuration
PLUGIN_PATHS = ['../../pelican-plugins']
PLUGINS = ['pandoc_reader']
PANDOC_ARGS = ['-f', 'markdown+smart',  # use smart typography
               '--no-highlight',  # use highlight.js instead
               '-t', 'html5',  # use HTML and its corresponding attributes
               '--section-divs',  # wrap heading-blocks with <section>
               '--filter', 'pandoc-citeproc']

# ----- Podcasting theme settings ----- #
import sys
import os
sys.path.append(os.getcwd())
from podcasting_theme import *
