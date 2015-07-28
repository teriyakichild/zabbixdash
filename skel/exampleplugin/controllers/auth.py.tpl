from {{ plugin_name }}.base import BaseHandler
import ldap
import tornado.web
import tornado.escape


class Edir(object):

    def __init__(self):
        self.groups = []

    def bind(self, username, password):
        l = ldap.initialize("ldaps://auth.edir.rackspace.com:636/")
        searchScope = ldap.SCOPE_SUBTREE
        baseDN      = "ou=Users,o=rackspace"
        try:
            l.simple_bind_s(
                "cn={username},ou=Users,o=rackspace".format(username=username),
                password
            )
            results = l.search(baseDN, searchScope, "cn=" + username)
        except Exception as e:
            print 'Error: %s' % e
            return False
        result_type, result_data = l.result(results)
        self.groups = result_data[0][1].setdefault('groupMembership', [])
        return True


class params(object):
    route = ['/auth',
             '/login']
    pass


class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self):
        error = self.get_argument('error', False)
        self.render('login.html', title='login', error=error)
        # self.write('success')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        e = Edir()
        next_page = self.get_argument("next", u"/")
        if e.bind(username, password):
            groups = e.groups
            self.set_current_user(username)
            print self.get_current_user()
            self.redirect(next_page)
        else:
            error_msg = u"?error=" + \
                tornado.escape.url_escape("Login incorrect.")
            self.redirect(u"/auth{0}".format(error_msg))
