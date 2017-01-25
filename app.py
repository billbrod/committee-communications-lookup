import os
import yaml
import requests
import pandas as pd
import tornado.ioloop as ti
from tornado.web import Application, RequestHandler
from numpy.random import randint

data_source_repo = 'https://raw.githubusercontent.com/unitedstates/congress-legislators/master'
current_legislators = data_source_repo + '/legislators-current.yaml'
ydat = yaml.load(requests.get(current_legislators).text)

class BaseHandler(RequestHandler):
    def get(self):
        self.render('index.html', data=ydat)

handles = [
    (r'/', BaseHandler),
    # (r'/', CommitteeDataHandler) # implement this to get filters for list
]

app_settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'debug': True,
    'cookie_secret': str(randint(1, 99999)),
}

def make_app():
    return Application(handles, **app_settings)

if __name__ == '__main__':
    app = make_app()
    app.listen(5000)
    ti.IOLoop.current().start()
