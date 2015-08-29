import os
import urllib

from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
	
class MainHandler(webapp2.RequestHandler):
    def get(self):
		template = JINJA_ENVIRONMENT.get_template('/index.html')
		self.response.write(template.render())
		
class Task(ndb.Model):
	title = ndb.StringProperty()
	description = ndb.StringProperty(indexed=False)	
	date = ndb.DateTimeProperty(auto_now_add=True)

class TaskHandler(webapp2.RequestHandler):	
	def post(self):
		print 'posted'
		

		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/task', TaskHandler),
], debug=True)
