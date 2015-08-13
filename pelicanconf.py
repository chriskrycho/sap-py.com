#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris and Jaimie Krycho'
SITENAME = 'Sap.py'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# ----- Podcasting theme settings ----- #
THEME = 'podcasting'
HEADER_LOGO_IMG = ''  # path to header logo image
HEADER_USE_LOGO_ONLY = False  # Don't use header text, just use the logo alone
NAV_LOGO_IMG = ''  # path to a square (minimum 128⨉128px) version of the logo
SUBTITLE = "Who says programming can't be romantic?"
