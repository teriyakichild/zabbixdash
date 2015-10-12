from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/actions'
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self):
        self.render(
            'actions.html',
            actions=self.alerts,
            title='actions'
        )

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
