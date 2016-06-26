# Example to create a table and dropdown menu using bokeh.  Currently,
# dropdown doesn't do antying. Also want to play around and see if I
# can use some custom css with this and embed within a flask app.

from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn, Dropdown
from bokeh.io import output_file, show, vform
import generate_fake_data
import pandas as pd
import os

output_file('test.html')

if not os.path.isfile("./dummy_data.csv"):
    generate_fake_data.main()
data = pd.read_csv("./dummy_data.csv", index_col=0)

source = ColumnDataSource(data)

columns = [
    TableColumn(field='names', title='Name'),
    TableColumn(field='age', title='Age'),
    TableColumn(field='birth_month', title='Birth Month'),
    TableColumn(field='gender', title='Gender'),
    TableColumn(field='origin', title='Country'),    
    ]

data_table = DataTable(source=source, columns=columns, width=1000, height=500)

menu = [("A", '1'), ("B", '2'), ("C", '3')]
dropdown = Dropdown(label="Please select", menu=menu)

show(vform(dropdown, data_table), browser='firefox')
