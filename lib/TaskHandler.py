import json
import webapp2
import logging
from lib.TaskRecord import TaskRecord
from lib.DateEncoder import DateEncoder


class TaskHandler(webapp2.RequestHandler):
    def post(self):
        logging.info("oi")
        task_request = json.loads(self.request.body)

        task_record = TaskRecord(title=task_request.get('title'), description=task_request.get('description'))

        task_record.put()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(task_record.to_dict(), cls=DateEncoder))