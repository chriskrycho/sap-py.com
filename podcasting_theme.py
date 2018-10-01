# coding: utf-8

"""
Define the Podcasting Theme configurable settings. You should import this in
your pelicanconf.py file -- it does not matter where in the file you import it.
"""

# You're welcome to rename the theme, of course; but if you change this without
# renaming the corresponding folder, things will get painful rather quickly.
THEME = 'podcasting-theme'

# Configure the header.
HEADER_LOGO_IMG = '/images/pythons_transp_512.png'  # path to header logo image
HEADER_USE_LOGO_ONLY = False  # Don't use header text, just use the logo alone
# Path from the root to a square (minimum 128⨉128px) version of the logo
NAV_LOGO_IMG = '/images/pythons_transp_128.png'
SUBTITLE = "Who says programming can't be romantic?"

# Configure the audio base audio URL. The full URL will be constructed as a
# path starting with this URL. For example, if in the article metadata you
# specify the `audio` value as `episode/05.mp3`, and this value were set to
# `http://cdn.my-site.com`, the full URL used in the template would be
# `https://cdn.my-site.com/episode/05.mp3`. It may be helpful to override this
# value in the production configuration (publishconf.py) and use local URLs
# for development or for validating a show before publishing it.
AUDIO_BASE_URL = 'https://www.podtrac.com/pts/redirect.m4a/f001.backblazeb2.com/file/sap-py'

# [Indie-web](https://indiewebcamp.com) identity setup
IDENTITY = {'Chris': 'http://www.chriskrycho.com/',
            'Jaimie': 'http://www.jaimiekrycho.com/'}

FOLLOW = {'iTunes': 'https://itunes.apple.com/us/podcast/sap.py/id1033841120?mt=2',
          'RSS': '/feed.xml',
          'Twitter': 'https://www.twitter.com/sappypodcast',
          'Overcast': 'https://overcast.fm/itunes1033841120/sap-py',
          'PocketCasts': 'http://pca.st/t583'}
