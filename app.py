#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# app.py
# TornadoBoilerplate
#
# Copyright 2014 Cole Maclean

import tornado.httpserver
import tornado.ioloop
import tornado.netutil
import tornado.web
from tornado.options import define, options

from settings import settings, locale_path
from urls import url_patterns

def run_server():
    """Run the server."""
    sockets = tornado.netutil.bind_sockets(options.port, address=options.ip)
    if options.processes != 1:
        tornado.process.fork_processes(options.processes)
    application = tornado.web.Application(url_patterns, **settings)
    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.add_sockets(sockets)
    tornado.locale.load_translations(locale_path)
    ioloop = tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run_server()
    