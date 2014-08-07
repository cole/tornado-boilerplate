#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# handlers.py
# TornadoBoilerplate
#
# Copyright 2014 Cole Maclean

import httplib

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """A class to collect common handler methods - all other handlers should
    subclass this one.
    """
    
    def write_error(self, status_code, **kwargs):
        """Display an error page. This will load the errors/{code}.html template if it exists,
        otherwise errors/error.html. (e.g, 404 will render errors/404.html)
        """
        try:
            error_template = "errors/" + str(status_code) + ".html"
            self.application.settings.get("template_loader").load(error_template)
            template = error_template
        except IOError:
            template = "errors/error.html"
        message = httplib.responses[status_code]
        self.render(template, code=status_code, message=message)
                    
    def get_url(self, *args, **kwargs):
        """Shortcut to reverse URLs.
        """
        return self.application.reverse_url(*args, **kwargs)

class NotFoundHandler(BaseHandler):
    """Catchall handler for unknown URLs.
    """
    
    def prepare(self):
        raise tornado.web.HTTPError(404)
        
class MainHandler(BaseHandler):
    """Home page handler. Here as a starting point.
    """
    
    def get(self):
        self.render('base.html')