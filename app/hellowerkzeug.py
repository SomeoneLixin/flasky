#!/usr/bin/env python
# encoding: utf-8
import os
from werkzeug.wrappers import BaseRequest, BaseResponse
from werkzeug.exceptions import HTTPException, MethodNotAllowed, \
     NotImplemented, NotFound
from werkzeug.serving import run_simple

class Request(BaseRequest):
    """Encapsulates a request."""


class Response(BaseResponse):
    """Encapsulates a response."""


class View(object):
    """Baseclass for our views."""
    def __init__(self):
        self.methods_meta = {
            'GET': self.GET,
            'POST': self.POST,
            'PUT': self.PUT,
            'DELETE': self.DELETE,
        }
    def GET(self):
        raise MethodNotAllowed()
    POST = DELETE = PUT = GET

    def HEAD(self):
        return self.GET()

    def dispatch_request(self, request, *args, **options):
        if request.method in self.methods_meta:
            return self.methods_meta[request.method](request, *args, **options)
        else:
            return '<h1>Unknown or unsupported require method</h1>'

    @classmethod
    def get_func(cls):
        def func(*args, **kwargs):
            obj = func.view_class()
            return obj.dispatch_request(*args, **kwargs)

        func.view_class = cls
        return func
class WebApp(object):
    def __init__(self):
        self.url_map = {}

    def __call__(self, environ, start_response):
        try:
            req = Request(environ)
            url = req.path
            view = self.url_map.get(url, None)
            if view:
                response = view(req)
                response = Response(response)
            else:
                response = Response('<h1>404 Source Not Found<h1>', content_type='text/html; charset=UTF-8', status=404)
        except HTTPException as e:
            response = e
        return response(environ, start_response)

    def add_url_rule(self,urls):
         for url in urls:
             self.url_map[url['url']] = url['view'].get_func()

    def run(self, port=5000, ip='', debug=False):
        run_simple(ip, port, self, use_debugger=debug, use_reloader=True)