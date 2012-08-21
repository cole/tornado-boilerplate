#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# app.py
# ProjectName
#
# Copyright 2012 Cole Maclean

import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from settings import settings
from urls import url_patterns

class Application(tornado.web.Application):
	"""Initialize our app, set up URLs and settings."""
	def __init__(self):
		tornado.web.Application.__init__(self, url_patterns, **settings)

if __name__ == "__main__":
	"""Run the server."""
	application = Application()
	tornado.locale.load_translations(application.settings.get("locale_path"))
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port, address=options.ip)
	io_loop = tornado.ioloop.IOLoop.instance()
	io_loop.start()