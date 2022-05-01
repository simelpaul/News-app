from flask import render_template
from app import app

@app.route("/")
def index():

    title = "Home - Welcome to the best News website online!"

    return render_template('home.html', title = title)

@app.route("/categories/<category>")
def categories(categories):

    return render_template("categories.html")