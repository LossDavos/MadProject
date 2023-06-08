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
    najlepsi =cur.execute("""SELECT   AVG(Medu), AVG(Fedu),AVG(traveltime), AVG(studytime) AS mean_studytime,
       AVG(failures) AS mean_failures,
       AVG(schoolsup) AS mean_schoolsup,
       AVG(famsup) AS mean_famsup,
       AVG(paid) AS mean_paid,
       AVG(activities) AS mean_activities,
       AVG(nursery) AS mean_nursery,
       AVG(higher) AS mean_higher,
       AVG(internet) AS mean_internet,
       AVG(romantic) AS mean_romantic,
       AVG(famrel) AS mean_famrel,
       AVG(freetime) AS mean_freetime,
       AVG(goout) AS mean_goout,
       AVG(Dalc) AS mean_Dalc,
       AVG(Walc) AS mean_Walc,
       AVG(health) AS mean_health,
       AVG(absences) AS mean_absences,
       AVG(G1) AS mean_G1,
       AVG(G2) AS mean_G2
FROM student_data WHERE G3>17;
""").fetchall()[0]
 
    vsetci = top_najlepsi =cur.execute("""SELECT   AVG(Medu), AVG(Fedu),AVG(traveltime), AVG(studytime) AS mean_studytime,
       AVG(failures) AS mean_failures,
       AVG(schoolsup) AS mean_schoolsup,
       AVG(famsup) AS mean_famsup,
       AVG(paid) AS mean_paid,
       AVG(activities) AS mean_activities,
       AVG(nursery) AS mean_nursery,
       AVG(higher) AS mean_higher,
       AVG(internet) AS mean_internet,
       AVG(romantic) AS mean_romantic,
       AVG(famrel) AS mean_famrel,
       AVG(freetime) AS mean_freetime,
       AVG(goout) AS mean_goout,
       AVG(Dalc) AS mean_Dalc,
       AVG(Walc) AS mean_Walc,
       AVG(health) AS mean_health,
       AVG(absences) AS mean_absences,
       AVG(G1) AS mean_G1,
       AVG(G2) AS mean_G2
FROM student_data;
""").fetchall()[0]
    najhorsi_0 = top_najlepsi =cur.execute("""SELECT   AVG(Medu), AVG(Fedu),AVG(traveltime), AVG(studytime) AS mean_studytime,
       AVG(failures) AS mean_failures,
       AVG(schoolsup) AS mean_schoolsup,
       AVG(famsup) AS mean_famsup,
       AVG(paid) AS mean_paid,
       AVG(activities) AS mean_activities,
       AVG(nursery) AS mean_nursery,
       AVG(higher) AS mean_higher,
       AVG(internet) AS mean_internet,
       AVG(romantic) AS mean_romantic,
       AVG(famrel) AS mean_famrel,
       AVG(freetime) AS mean_freetime,
       AVG(goout) AS mean_goout,
       AVG(Dalc) AS mean_Dalc,
       AVG(Walc) AS mean_Walc,
       AVG(health) AS mean_health,
       AVG(absences) AS mean_absences,
       AVG(G1) AS mean_G1,
       AVG(G2) AS mean_G2
FROM student_data WHERE G3=0;
""").fetchall()[0]
    najhorsi_nie_0 = top_najlepsi =cur.execute("""SELECT   AVG(Medu), AVG(Fedu),AVG(traveltime), AVG(studytime) AS mean_studytime,
       AVG(failures) AS mean_failures,
       AVG(schoolsup) AS mean_schoolsup,
       AVG(famsup) AS mean_famsup,
       AVG(paid) AS mean_paid,
       AVG(activities) AS mean_activities,
       AVG(nursery) AS mean_nursery,
       AVG(higher) AS mean_higher,
       AVG(internet) AS mean_internet,
       AVG(romantic) AS mean_romantic,
       AVG(famrel) AS mean_famrel,
       AVG(freetime) AS mean_freetime,
       AVG(goout) AS mean_goout,
       AVG(Dalc) AS mean_Dalc,
       AVG(Walc) AS mean_Walc,
       AVG(health) AS mean_health,
       AVG(absences) AS mean_absences,
       AVG(G1) AS mean_G1,
       AVG(G2) AS mean_G2
FROM student_data WHERE (G3 >= 4 AND G3 <= 6);
""").fetchall()[0]
    options = ["Medu", "Fedu", "traveltime", "studytime", "failures", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2"]
    return render_template('results.html', graphJSON=graphJSON, header=header,description=description, points = points, info_cat=cursor.fetchall(),
                           najlepsi = najlepsi, vsetci = vsetci, najhorsi_0 = najhorsi_0, najhorsi_nie_0 = najhorsi_nie_0, options = options)

    # return render_template("results.html")

@app.route('/tiy')
def tyi():
    return render_template("tyi.html")

if __name__ == '__main__':
    app.run(debug=True)
