# Standard Library
import functools
import urlparse
from urllib import urlencode

# Packages
import tornado.web
import tornado.escape
from myui import create_tables
from zabbixdash import __version__ as VERSION
from zabbixdash import ui_modules
from pyzabbix import ZabbixAPI

cursors = create_tables(get_settings=False)

class BaseHandler(tornado.web.RequestHandler):
    zabbix_handles={}
    dashboards={}
    cache={}

    def data_received(self, chunk):
        super(BaseHandler, self).data_received(chunk)

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        # Load Config from tornado settings
        self.config = self.settings['plugin_opts'].get('zabbixdash', {})
        self.config.setdefault('session', {})

        # Session timeout and other defaults
        self.config['session']['expires_days'] = self.config['session'].get('expires_days', None)
        self.config['session']['max_age_days'] = self.config['session'].get('max_age_days', 1)

        self.Dashboard = cursors['dashboards'][0]
        self.User = cursors['dashboards'][1]
        self.Server = cursors['dashboards'][2]

        # Create Zabbix Handles from the config file
        for endpoint in self.config['endpoints']:
            if not self.zabbix_handles.get(endpoint['uri'], False):
                self.set_zabbix_handle(
                    endpoint['uri'],
                    endpoint['user'],
                    endpoint['pass'],
                    endpoint['ssl_verify']
                )

                # Create the zabbix host cache
                self.zapi_cache(
                    endpoint['uri'],
                    'host',
                    {'output': ['available', 'host', 'status', 'hostid', 'proxy_hostid', 'error']}
                )
                # Create the zabbix action cache
                self.zapi_cache(
                    endpoint['uri'],
                    'action',
                    {'output': ['available', 'host', 'status', 'hostid', 'proxy_hostid', 'error']}
                )

        self.nav_links = [
            ('Home', '/'),
            ('Link2', '#Link2')
        ]

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            user = None
        return user

    def set_current_user(self, username):
        if username is None:
            self.clear_cookie("user")
            return False
        self.set_secure_cookie("user", str(username), expires_days=self.config['session']['expires_days'])
        self.User.create(name=username)
        return True

    def set_zabbix_handle(self, host, user, password, ssl_verify):
        if not self.zabbix_handles.get(host, False):
            zapi = ZabbixAPI(host)
            zapi.session.verify = ssl_verify
            zapi.login(user, password)

            self.Server.create(host=host, token=zapi.auth)
            self.zabbix_handles[host] = zapi
            ret = zapi
        else:
            ret = self.zabbix_handles[host]
        return ret

    def get_zabbix_handle(self, host):
        if not self.zabbix_handles.get(host, False):
            return None
        else:
            return self.zabbix_handles[host]

    def update_hostcache(self, host, zapi):
        self.hosts[host] = zapi.host.get(output=['available', 'host', 'status', 'hostid', 'proxy_hostid', 'error'])

    def update_actioncache(self, host, zapi):
        'status', 'def_shortdata', 'name', 'esc_period', 'evaltype', 'def_longdata', 'eventsource', 'actionid', 'r_shortdata', 'r_longdata', 'recovery_msg'
        self.actions[host] = zapi.action.get(output='extend')

    def zapi_cache(self, host, method, args):
        z = self.zabbix_handles.get(host, False)
        if z:
            try:
                ret = getattr(z, method).get(**args)
            except Exception as e:
                if 'Not Authorized' in str(e):
                    endpoint = [endpoint for endpoint in self.config['endpoints'] if endpoint['name'] == host][0]
                    z.login(endpoint['user'], endpoint['password'])
                    ret = getattr(z, method).get(**args)
                else:
                    ret = []
            self.cache.setdefault(method, {})[host] = ret

    def render(self, template_name, **kwargs):
        """ We are overriding the render method in order to provide common objects
        to the templates.  (ie. Navigation Links, Version number) """

        # Add VERSION to kwargs
        kwargs['VERSION'] = VERSION

        # Add app_title from config file
        kwargs['app_title'] = self.settings['app_title']

        # Add self.nav_links, which is set in __init__() above,  to kwargs
        kwargs['nav_links'] = kwargs.get('nav_links', self.nav_links)

        kwargs['zabbix_handles'] = self.zabbix_handles

        super(BaseHandler, self).render(template_name, **kwargs)
