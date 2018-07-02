# coding:utf-8

import tornado
import tornado.web
import tornado.httpserver
import json
import tornado.escape
import tornado.ioloop

from tornado.options import define,options
from tornado.web import RequestHandler,url

# 定义全局设置
define("port", default=8080, type=int)

class PostView(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("post.html")

class IndexView(RequestHandler):
    def post(self, *args, **kwargs):
        print(self._headers)
        #data = tornado.escape.json_decode("{\"name\":\"yuki\"}")
        data = self.request.body.decode("utf-8")
        data = tornado.escape.json_decode(data)
        print(type(data))
        print(type(tornado.escape.json_decode(data)))
        self.write(">_<")
        self.finish()

    def get(self, *args, **kwargs):
        self.write("get")
        self.finish()

if __name__ == '__main__':
    options.parse_command_line()
    app = tornado.web.Application([
        url(r'/index',IndexView),
        url(r'/post', PostView)
    ])

    app.listen(options.port)

    server = tornado.httpserver.HTTPServer(app)
    tornado.ioloop.IOLoop.current().start()