#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# handlers.py
# ProjectName
#
# Copyright 2012 Cole Maclean

import httplib

import tornado.web
import tornado.websocket
import tornado.locale
import tornado.ioloop
import tornado.httpclient

class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """

    def prepare(self):
        """Handle 'flash' notifications, a la Rails."""
        self.flash = {}
        self.flash['error'] = self.get_argument("error", None)
        self.flash['notice'] = self.get_argument("notice", None)
    
    def get_user_locale(self):
        """Returns user's locale.
        """
        return None
    
    def write_error(self, status_code, **kwargs):
        """Display a custom error page.
        """
        try:
            error_template = "errors/" + str(status_code) + ".html"
            self.application.settings.get("template_loader").load(error_template)
            template = error_template
        except IOError:
            template = "errors/default.html"
        
        self.render(template, code=status_code, message=httplib.responses[status_code])

class NotFoundHandler(BaseHandler):
    """Catchall handler for unknown URLs.
    """
    
    def prepare(self):
        raise tornado.web.HTTPError(404)
        
class MainHandler(BaseHandler):
    """Home page handler
    """
    
    def get(self):
        self.render('base.html')