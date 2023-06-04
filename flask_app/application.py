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
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

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
