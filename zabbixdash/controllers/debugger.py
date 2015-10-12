from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/pdb'
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self):
        if self.settings['debug']:
            import pdb;pdb.set_trace()

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
