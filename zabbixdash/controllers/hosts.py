from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = '/hosts'
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self):
        self.render(
            'hosts.html',
            hosts=self.cache['host'],
            states=[
                {
                    'text': 'unknown',
                    'color': 'yellow'
                },
                {
                    'text': 'available',
                    'color': 'green'
                },
                {
                    'text': 'unavailable',
                    'color': 'red'
                }
            ],
            title='hosts'
        )

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
