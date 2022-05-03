from flask import render_template
# import main
from app import app 
from .request import get_all_articles
# from models import Article

@app.route('/')
@app.route('/index')
def index():
    articles = get_all_articles()
    print(articles)
    return render_template('index.html', articles=articles )



