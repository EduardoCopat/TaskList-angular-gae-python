import os
import urllib

from google.appengine.ext import ndb

import jinja2
import webapp2
import logging
import json

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('/index.html')
        self.response.write(template.render())


class TaskRecord(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class TaskHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("debugano")
        logging.info(self.request.body)
        taskRequest = json.loads(self.request.body)
        
        taskRecord = TaskRecord(title=taskRequest.get('title'), description=taskRequest.get('description'))

        taskRecord.put()
        return


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/task', TaskHandler),
], debug=True)
