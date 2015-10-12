__all__ = ['Table']
import tornado.web

class Table(tornado.web.UIModule):
    def render(self, objects, display_keys=False):
        if not display_keys:
            display_keys = objects[0].keys()

        return self.render_string("table_ui_module.html", objects=objects, display_keys=display_keys)
