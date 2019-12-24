"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from bson.json_util import dumps 
from FamilyFeud import app
from pymongo import MongoClient 
import random 

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
