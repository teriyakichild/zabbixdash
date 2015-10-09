from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/add_zabbix_handle'
    pass


class Handler(BaseHandler):

    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self):
        self.render(
            'add_zabbix_handle.html',
            title='main'
        )

    @tornado.web.authenticated
    def post(self):
        self.set_zabbix_handle(
            self.get_argument('host', None),
            self.get_argument('user', None),
            self.get_argument('password', None)
        )
        self.redirect('/')
