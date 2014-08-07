#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# settings.py
# TornadoBoilerplate
#
# Copyright 2014 Cole Maclean

import os
import logging

from tornado.template import Loader
from tornado.locale import set_default_locale
from tornado.options import define, options, parse_command_line

debug = True # Enable debug/dev mode

define("ip", default="127.0.0.1", help="run on the given ip address")
define("port", default=8888, help="run on the given port", type=int)
define('processes', default=0, help="number of processes to fork (0 = number of CPUs)", type=int)

parse_command_line()

ROOT = os.path.dirname(os.path.abspath(__file__))
locale_path = os.path.join(ROOT, 'locale')
template_path = os.path.join(ROOT, 'templates')
static_path = os.path.join(ROOT, 'static')

settings = {
    'debug': debug,
    'log_level': logging.DEBUG if debug else logging.INFO,
    'locale_path': locale_path,
    'template_path': template_path,
    'static_path': static_path,
    'static_url_prefix': "/static/",
    'template_loader': Loader(template_path),
    'xsrf_cookies': True,
    'cookie_secret': "__TODO:__REPLACE_ME_WITH_A_RANDOM_VALUE__"
}

set_default_locale('en_US')

logging.getLogger().setLevel(settings['log_level'])
