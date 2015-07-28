# Standard Library
import functools
import urlparse
from urllib import urlencode

# Packages
import tornado.web
import tornado.escape
from exampleplugin import __version__ as VERSION


class BaseHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        super(BaseHandler, self).data_received(chunk)

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

        self.nav_links = [
            ('Link 1', '#Link1'),
            ('Link 2', '#Link2')
        ]

    def get_current_user(self):
        user = self.get_secure_cookie("user")
        if not user:
            user = None
        return user

    def set_current_user(self, username):
        print username
        if username is None:
            self.clear_cookie("user")
            return False
        self.set_secure_cookie("user", str(username))
        return True

    def render(self, template_name, **kwargs):
        """ We are overriding the render method in order to provide common objects
        to the templates.  (ie. Navigation Links, Version number) """

        # Add VERSION to kwargs
        kwargs['VERSION'] = VERSION

        # Add self.nav_links, which is set in __init__() above,  to kwargs
        kwargs['nav_links'] = kwargs.get('nav_links', self.nav_links)

        super(BaseHandler, self).render(template_name, **kwargs)
