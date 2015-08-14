#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris and Jaimie Krycho'
SITENAME = 'Sap.py'
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

# Configure the audio base audio URL. The full URL will be constructed as a
# path starting with this URL. For example, if in the article metadata you
# specify the `audio` value as `episode/05.mp3`, and this value were set to
# `http://cdn.my-site.com`, the full URL used in the template would be
# `https://cdn.my-site.com/episode/05.mp3`. It may be helpful to override this
# value in the production configuration (publishconf.py) and use local URLs
# for development or for validating a show before publishing it.
AUDIO_BASE_URL = '//cdn.sap-py.com'

# [Indie-web](https://indiewebcamp.com) identity setup
IDENTITY = {'Chris': 'http://www.chriskrycho.com/',
            'Jaimie': 'http://www.jaimiekrycho.com/',
            'Twitter': 'https://www.twitter.com/sappypodcast',
            'App.net': 'https://alpha.app.net/sappy'}
