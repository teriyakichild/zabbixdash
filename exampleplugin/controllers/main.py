from exampleplugin.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/'
    pass


class Handler(BaseHandler):

    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self):
        self.render(
            'main.html',
            title='main'
        )

    @tornado.web.authenticated
    def post(self):
        self.redirect('/')
