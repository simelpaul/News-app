from flask import render_template
from app import app

@app.route("/")
def index():

    return render_template('home.html')

@app.route("/categories/<category>")
def categories(categories):
    
    return render_template("categories.html")