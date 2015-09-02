import os

import jinja2
import webapp2
from lib.TaskHandler import TaskHandler
from lib.TasksHandler import TasksHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/task', TaskHandler),
    ('/tasks', TasksHandler),
], debug=True)
