#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# urls.py
# ProjectName
#
# Copyright 2012 Cole Maclean

from tornado.web import URLSpec, ErrorHandler
from handlers import *

url_patterns = [
    URLSpec(r"/", MainHandler, name="root"),
]