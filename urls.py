#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# urls.py
# TornadoBoilerplate
#
# Copyright 2014 Cole Maclean

from tornado.web import url
from handlers import MainHandler, NotFoundHandler

url_patterns = [
    url(r"/", MainHandler, name="root"),
    url(r"/(.*)", NotFoundHandler, name='404') # should always be last
]