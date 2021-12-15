# Import flask and other libraries
#from models import create_classes
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
#import pandas as pd

#from sqlalchemy import create_engine
#from flask_sqlalchemy import SQLAlchemy

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '').replace("postgres://", "postgresql://", 1)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#News = create_classes(db)

# create route that renders index.html template
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

# Run app
if __name__ == "__main__":
    app.run(debug=True)