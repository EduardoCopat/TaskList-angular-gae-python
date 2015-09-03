import json

import webapp2
from src.lib.TaskRecord import TaskRecord
from src.lib.DateEncoder import DateEncoder


class TasksHandler(webapp2.RequestHandler):
    def get(self):
        tasks = TaskRecord.query().order(TaskRecord.date)
        tasks_json = []
        for task in tasks:
            tasks_json.append(task.to_dict())

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(
            json.dumps(tasks_json, cls=DateEncoder))  # We need to use a custom DateEncoder to handle Dates in NDB