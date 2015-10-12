from zabbixdash.base import BaseHandler
import tornado.web
from datetime import datetime


class params(object):
    route = ['/compare',
            '/compare/([a-z]+)',
            '/compare/([a-z]+)/([a-z]+)']
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    @tornado.web.authenticated
    def get(self, method='host', unique_key=False):
        args = {}
        if not unique_key:
            unique_key = 'name'

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
            'compare.html',
            results=results,
            unique_key=unique_key,
            hosts=hosts,
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
            title='compare'
        )

    #@tornado.web.authenticated
    def post(self):
        self.redirect('/')
