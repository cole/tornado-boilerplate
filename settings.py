#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# settings.py
# ProjectName
#
# Copyright 2012 Cole Maclean

import tornado
import tornado.template
import os
import logging
from tornado.options import define, options

define("ip", default="127.0.0.1", help="run on the given ip address")
define("port", default=8888, help="run on the given port", type=int)

tornado.options.parse_command_line()

ROOT = os.path.dirname(os.path.abspath(__file__))

settings = dict(
    site_title=u"ProjectName",
    log_level=logging.DEBUG,
    locale_path=os.path.join(ROOT, 'locale'),
    template_path=os.path.join(ROOT, 'template'),
    static_path=os.path.join(ROOT, 'static'),
    static_url_prefix="/static/",
    template_loader=tornado.template.Loader(os.path.join(ROOT, 'templates')),
    xsrf_cookies=True,
    cookie_secret="ot8bi6trif2pog2baf8uc7fem9ob5af4wob2ac3nab4vuj9dy6",
)

logging.getLogger().setLevel(settings['log_level'])
