import generate_fake_data
from flask import *
import pandas as pd
import os
app = Flask(__name__)

if not os.path.isfile("./dummy_data.csv"):
    generate_fake_data.main()
data = pd.read_csv('dummy_data.csv', index_col=0)

@app.route("/")
def show_tables():
    return render_template('view.html',tables=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)
