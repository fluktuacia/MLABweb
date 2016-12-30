#!/usr/bin/python
# -*- coding: utf-8 -*-
import tornado
#from tornado import web
from tornado import ioloop
from tornado import auth
from tornado import escape
from tornado import httpserver
from tornado import options
from tornado import web
import json
#import sqlite3
import MySQLdb as mdb
import time
import datetime
import calendar


from handlers import *
from handlers import _sql, BaseHandler, basic


tornado.options.define("port", default=10010, help="port", type=int)
tornado.options.define("debug", default=True, help="debug mode")

class WebApp(tornado.web.Application):
    def __init__(self, config={}):

        name = 'MLAB'
        server = 'meteor2.astrozor.cz'

        server_url = '{}:{}'.format(server, tornado.options.options.port)

        handlers =[
            (r'/', WebHandler),
            (r"/(.*)", WebHandler),
        ]
        settings = dict(
            cookie_secret="ROT13IrehaxnWrArwyrcfvQvixnAnFirgr",
            #template_path= "/home/roman/repos/RTbolidozor/template/",
            #static_path= "/home/roman/repos/RTbolidozor/static/",
            xsrf_cookies=True,
            name=name,
            server_url=server_url,
            site_title=name,
            login_url="/login",
            #ui_modules=modules,
            port=tornado.options.options.port,
            compress_response=True,
            debug=tornado.options.options.debug,
            autoreload=True
        )

        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    import os
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(WebApp())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
