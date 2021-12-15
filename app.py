# Import dependencies
import os
import pandas as pd
import pickle
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, or_
from sqlalchemy.ext.automap import automap_base
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from sqlalchemy import create_engine

# Create instance of Flask app
app = Flask(__name__)

POSTGRES_USER = "postgres"
POSTGRES_PW = "postgres"
POSTGRES_URL = "fake-news-prediction-db.citnkkc6ztdk.us-east-2.rds.amazonaws.com"
POSTGRES_DB = "project4DB"

# Set up connection
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:' +
    f'{os.getenv("POSTGRES_PW")}@{os.getenv("POSTGRES_URL")}/{os.getenv("POSTGRES_DB")}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Define what to do when a user hits the /visuals route
@app.route("/visuals")
def visuals():
    return render_template("visuals.html")

# Define what to do when a user hits the /model route
@app.route("/form") #, methods=['POST', 'GET']
def form():
    #if request.method == "POST":
        #search_content = request.form['predictfakenews']
    #else: 
    return render_template("form.html")


@app.route("/model" , methods=["POST"])
def model():
    filename = './models/logistic_regression.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    #prediction = loaded_model.predict(X)[0][0]

    print(prediction)

    return render_template("form.html", prediction = prediction)


# Run app
if __name__ == "__main__":
    app.run(debug=True)