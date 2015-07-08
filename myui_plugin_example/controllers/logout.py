from myui_plugin_example.base import BaseHandler
import tornado.web


class params(object):
    route = ['/logout']
    pass


class Handler(BaseHandler):

    @tornado.web.removeslash
    def get(self):
        self.clear_cookie("user")
        self.redirect(u"/login")
