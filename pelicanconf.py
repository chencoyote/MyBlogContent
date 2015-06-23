#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'coyote'
SITENAME = u"Coyote's Blog"
SITEURL = 'http://chencoyote.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

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
SOCIAL = (('Github','https://github.com/chencoyote'),
          ('Google+', 'https://plus.google.com/u/0/104542842241928417898/posts'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Content path
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
      'files/robots.txt': {'path': 'robots.txt'},
      'images/favicon.ico': {'path': 'favicon.ico'},
}

# URL settings
ARTICLE_URL = ('articles/{slug}.html')
ARTICLE_SAVE_AS = ('articles/{slug}.html')
PAGE_LANG_SAVE_AS = False

# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme
THEME = '/home/chen/selfsoft/pelican-themes/pelican-sober'
COVER_BG_COLOR = '#375152'
DEFAULT_PAGINATION = 10

# Plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap', 'gravatar' ]

# Sitemap
SITEMAP = {
  'format': 'xml',
  'priorities': {
      'articles': 1,
      'pages': 0.9,
      'indexes': 0.8,
  },
  'changefreqs': {
      'indexes': 'daily',
      'articles': 'daily',
      'pages': 'weekly'
  }
}
