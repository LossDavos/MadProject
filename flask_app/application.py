import json
from flask import Flask, render_template,g
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

app = Flask(__name__)


def connect_db():
    return sqlite3.connect('students.db')

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/results')
def results():
    cur = g.db.cursor()
    df = px.data.iris()
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
    x1 = np.ones(100) + 5
    y1 = np.linspace(1, 5, 100)
    z1 = np.linspace(0, 3, 50)
    rc = np.ones(100) + 40
    plane = go.Surface(x=x1, y=y1, z=np.array([z1] * len(x1)), surfacecolor=rc, showscale=False)
    fig.add_traces([plane])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """


    #information about the individual categories
    # connect to a database 
    connection = sqlite3.connect('students.db')
    # create a "cursor" for working with the database
    cursor = connection.cursor()
    
    cursor.execute("""SELECT Test, Group1, Group2, Estimate1, Estimate2, Statistic, p_value FROM t_tests""") 

    points = cur.execute("SELECT G3, COUNT(*) AS group_size FROM student_data GROUP BY G3").fetchall()
    return render_template('results.html', graphJSON=graphJSON, header=header,description=description, points = points, info_cat=cursor.fetchall())

    # return render_template("results.html")

@app.route('/tiy')
def tyi():
    return render_template("tyi.html")

if __name__ == '__main__':
    app.run(debug=True)
