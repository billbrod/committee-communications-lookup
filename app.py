import os
import yaml
import pandas as pd
import tornado.ioloop as ti
from tornado.web import Application, RequestHandler
from numpy.random import randint

with open('data/legislators-current.yaml', 'r') as f:
    df = pd.io.json.json_normalize(yaml.load(f))

terms = [pd.DataFrame(i) for i in df['terms']]
terms = pd.concat([t.loc[t.index[-1]] for t in terms], axis=1).T 
commdata = terms.to_html()

class BaseHandler(RequestHandler):
    def get(self):
        self.render('index.html', data=commdata)

handles = [
    (r'/', BaseHandler),
    # (r'/', CommitteeDataHandler)
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


# import generate_fake_data
# from flask import *
# import pandas as pd
# import os
# app = Flask(__name__)
#
# if not os.path.isfile("./dummy_data.csv"):
#     generate_fake_data.main()
# data = pd.read_csv('dummy_data.csv', index_col=0)
#
# @app.route("/")
# def show_tables():
#     return render_template('view.html', tables=data.to_html())
#
# if __name__ == "__main__":
#     app.run(debug=True)
