import os
from google.appengine.ext import ndb
import urllib

import jinja2
import webapp2
import logging
import json

import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("oi1")
        template = JINJA_ENVIRONMENT.get_template('index.html')
        logging.info("oi2")
        self.response.write(template.render())


class TaskRecord(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class TaskHandler(webapp2.RequestHandler):
    def post(self):
        logging.info(self.request.body)
        taskRequest = json.loads(self.request.body)

        taskRecord = TaskRecord(title=taskRequest.get('title'), description=taskRequest.get('description'))

        taskRecord.put()
        return



class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


class TasksHandler(webapp2.RequestHandler):
    def get(self):
        tasks = TaskRecord.query().fetch()
        tasks_json = []
        for task in tasks:
            tasks_json.append(task.to_dict())

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(tasks_json,  cls=DateEncoder)) #We need to use a custom DateEncoder to handle Dates in NDB


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/task', TaskHandler),
    ('/tasks', TasksHandler),
], debug=True)
