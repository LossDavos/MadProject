import json
from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/results')
def results():
    df = px.data.iris()
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Fruit in North America"
    description = """
    A academic study of the number of apples, oranges and bananas in the cities of
    San Francisco and Montreal would probably not come up with this chart.
    """
    return render_template('results.html', graphJSON=graphJSON, header=header,description=description)

    # return render_template("results.html")

@app.route('/tiy')
def tyi():
    return render_template("tyi.html")

if __name__ == '__main__':
    app.run(debug=True)
