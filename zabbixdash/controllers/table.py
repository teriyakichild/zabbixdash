from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = ['/table',
            '/table/([a-z]+)',
            '/table/([a-z]+)/([0-9]+)']
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self, method='host', limit=None):
        args = {}
        if limit:
            args['limit'] = limit

        args['output'] = 'extend'
            
        results = []
        for host, zapi in self.zabbix_handles.iteritems():
            tmp = getattr(zapi, method).get(**args)
            for each in tmp:
                each['zabbixhost'] = host
                results.append(each)
        self.render(
            'table.html',
            objects=results,
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
            title='actions'
        )

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
