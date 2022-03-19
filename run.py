# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpserver

import config as CONFIG
from reply import WxSignatureHandler

patterns = [
            tornado.web.url(r"/.*", WxSignatureHandler)
]

def main():
    application = tornado.web.Application(handlers=patterns, **CONFIG.settings)
    http_server = tornado.httpserver.HTTPServer(application)
    print("start")
    http_server.listen(CONFIG.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
