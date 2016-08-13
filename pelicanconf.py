#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '크래커'
SITENAME = 'Red2.net'
#SITEURL = 'http://red2.net' # PRODUCTION
SITEURL = 'http://localhost:8000' # TEST

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = []

# Social widget
SOCIAL = []
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# New things for RED2.net

# date format
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ko': '%Y-%m-%d (%a)',
    'jp': '%Y-%m-%d (%a)'
}

# Thins to copy to output
STATIC_PATHS = [
    'images',
    'extra/red2fav.ico'
]

# Copy destination
EXTRA_PATH_METADATA = {
        'extra/red2fav.ico': {'path': 'favicon.ico'}
}

# Theme settings
THEME = './themes/red2'
RED2_FAVICON = '/red2fav.ico' # be sure to update STATIC_PATHS and EXTRA_PATH_METADATA.
#DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [
    ('메인', '/#'),
    ('게임', '/game.html'),
    ('컨텐츠', '/contents.html'),
    ('커뮤니티', '/#'),
    ('자료실', '/#'),
    ('사이트', '/#')
]
# Note: you specify save_as meta data in wiki.md to generate wiki.html!
# That's how you get expectable file names for the MENUITEMS.

# Feed
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 100
FEED_ALL_ATOM = 'feeds/all.atom.xml'
