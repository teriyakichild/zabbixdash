from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/dashboard/([0-9]+)'
    pass


class Handler(BaseHandler):

    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self, id):
        print self.dashboards 
        self.render(
            'dashboard.html',
            dashboard=self.dashboards[id],
            title='dashboard'
        )

    @tornado.web.authenticated
    def post(self):
        self.redirect('/')
