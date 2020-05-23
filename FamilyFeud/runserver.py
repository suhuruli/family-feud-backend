"""
This script runs the FamilyFeud application using a development server.
"""

from os import environ

from datetime import datetime
from flask import Flask, render_template
from bson.json_util import dumps 
from pymongo import MongoClient 
import random 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/threeanswer', methods=['GET'])
def threeanswer():
    client = MongoClient('mongodb://suhurulitest:t03pD6vZB7gHPNgyy3XpTojdY0DtBfQdBvz8sZui4guf9eY01tlr41Q5Ne6MtdXKYAToZhEYj2WQovchHeij0A==@suhurulitest.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'); 
    db = client.familyfeuddb; 
    collection = db.threeanswers; 
    num = random.randint(1,90);
                    
    threeanswer = collection.find({"questionID" : num}); 

    resp = dumps(threeanswer); 
    return resp;

@app.route('/fouranswer', methods=['GET'])
def fouranswer():
    client = MongoClient('mongodb://suhurulitest:t03pD6vZB7gHPNgyy3XpTojdY0DtBfQdBvz8sZui4guf9eY01tlr41Q5Ne6MtdXKYAToZhEYj2WQovchHeij0A==@suhurulitest.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'); 
    db = client.familyfeuddb; 
    collection = db.fouranswers; 
    num = random.randint(1,90);
                    
    fouranswer = collection.find({"questionID" : num}); 

    resp = dumps(fouranswer); 
    return resp; 

@app.route('/fiveanswer', methods=['GET'])
def fiveanswer():
    client = MongoClient('mongodb://suhurulitest:t03pD6vZB7gHPNgyy3XpTojdY0DtBfQdBvz8sZui4guf9eY01tlr41Q5Ne6MtdXKYAToZhEYj2WQovchHeij0A==@suhurulitest.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'); 
    db = client.familyfeuddb; 
    collection = db.fiveanswers; 
    num = random.randint(1,90);
                    
    fiveanswer = collection.find({"questionID" : num}); 

    resp = dumps(fiveanswer); 
    return resp; 

@app.route('/fastmoney', methods=['GET'])
def fastmoney():
    client = MongoClient('mongodb://suhurulitest:t03pD6vZB7gHPNgyy3XpTojdY0DtBfQdBvz8sZui4guf9eY01tlr41Q5Ne6MtdXKYAToZhEYj2WQovchHeij0A==@suhurulitest.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'); 
    db = client.familyfeuddb; 
    collection = db['fast-money']; 
    num = random.randint(1,90);
                    
    fastmoney = collection.find({"questionID" : num}); 

    resp = dumps(fastmoney); 
    return resp; 

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
