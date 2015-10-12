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
        results = {}
        hosts = []
        for host in self.zabbix_handles:
            hosts.append(host)
            self.zapi_cache(host, method, args)
            objects = self.cache.get(method, {}).get(host, [])
            for each in objects:
                results.setdefault(each[unique_key], {})[host] = True
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
