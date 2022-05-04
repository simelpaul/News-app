from flask import render_template
# import main
from app import app 
from .request import get_all_articles, get_all_sources
# from models import Article

@app.route('/')
@app.route('/index')
def index():
    articles = get_all_articles()
    sources = get_all_sources()
    print(articles)
    return render_template('index.html', articles=articles, sources=sources)

# @app.route('/')
# @app.route('/sources')
# def sources():
#     sources = get_all_sources()
#     print(sources)
#     return render_template('index.html', sources=sources )


