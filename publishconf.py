#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://Vlad-Duda.me'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Categories
DEFAULT_CATEGORY = 'Thoughts'

# Following items are often useful when publishing

GITHUB_URL = "https://github.com/VDuda"
DISQUS_SITENAME = "vlad-duda.disqus.com"
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True
#GOOGLE_ANALYTICS = ""