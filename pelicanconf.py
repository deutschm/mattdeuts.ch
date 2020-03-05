#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Matt Deutsch'
SITENAME = u'Matt\'s Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Dallas'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

USE_FOLDER_AS_CATEGORY = False

# STATIC_PATHS = [
#     'content/admin/config.yml',
#     ]

TEMPLATE_PAGES = {'admin/index.html': 'admin/index.html'}
STATIC_PATHS = ['uploads', 'admin']

CMS_ENV = "development"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
