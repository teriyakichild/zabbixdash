from zabbixdash.base import BaseHandler
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
            hosts=self.hosts,
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
            title='main'
        )

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
