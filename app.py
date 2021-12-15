# Import flask and other libraries
#from models import create_classes
import os

import pickle
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize

model_logistc = pickle.load(open("models/logistic_regression.sav", "rb"))

#functions

def lemmatize_sentence(text):
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    sentence = ""
    
    # Tokenization
    words = nltk.word_tokenize(text)
    # Stopwords removal
    words = [w for w in words if not w in stop_words]
    # Lemmatization
    for word in words:
        sentence = sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
        
    sentence = [sentence]
        
    return sentence

def vectorize_sentence(sentence):
    freq_term_matrix = count_vectorizer.transform(sentence)

    tfidf = TfidfTransformer(norm = "l2")
    tfidf.fit(freq_term_matrix)
    tf_idf_matrix = tfidf.fit_transform(freq_term_matrix)
    
    return tf_idf_matrix

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

@app.route("/form")
def form():
    return render_template("form.html", model_result = " ")

# Define what to do when a user hits the /model route
@app.route("/send",  methods=['POST'])
def send():
    #print('hello')
    new_text = request.form["predictfakenews"]
    print(new_text)

    vect_text = vectorize_sentence(lemmatize_sentence(new_text))

    

    result = "Fake"

    return render_template("form.html", model_result = result)

# Run app
if __name__ == "__main__":
    app.run(debug=True)