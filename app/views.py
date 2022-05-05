from flask import render_template
# import main
from app import app 
from .request import get_all_articles, get_all_sources
# from models import Article

@app.route('/')
@app.route('/index')
def index():
    sources = get_all_sources()
    articles = get_all_articles()
    return render_template('index.html', articles=articles, sources = sources)

