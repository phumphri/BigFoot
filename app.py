# import necessary libraries
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db/bigfoot.sqlite")
# engine = create_engine("sqlite:///C:/Users/Patrick/OneDrive/A/01-Class-Content/15-Interactive-Visualizations-and-Dashboards/3/Activities/Unsolved/04-Stu_Bigfoot/db/bigfoot.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table
Bigfoot = Base.classes.bigfoot

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Query the database and send the jsonified results
@app.route("/data")
def data():

    # @TODO: Use a database query to fetch the results and send
    # the data to your plot
    # Note:  Group by year of timestamp, count timestamps
    sel = [func.strftime("%m", Bigfoot.timestamp), func.count(Bigfoot.timestamp)]


    results = session.query(*sel).group_by(func.strftime("%m", Bigfoot.timestamp)).all()



    # @TODO: YOUR CODE HERE

    # results is a list of sets.  Each set is a string year and a numeric count.
    print("results:")
    print(results)

    return jsonify(results)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    # from os import environ
    # app.run(debug=False, host='0.0.0.0', port=environ.get("PORT", 5000))
    # app.run(debug=False, host='0.0.0.0', port=5000)
    app.run(debug=False)
    