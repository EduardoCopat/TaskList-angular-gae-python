from google.appengine.ext import ndb

class TaskRecord(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
