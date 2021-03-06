import os
import urllib.request, json, urllib
from app.config import Config
from .models import Article, Sources

api_key = None
base_url = None

api_key = os.environ.get('NEWS_API_KEY')

def get_all_articles():

    # all_articles = newsapi.get_everything(q='bitcoin',sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com',from_param='2022-04-18',to='2022-05-03',language='en',sort_by='relevancy')

    get_articles_url = 'https://newsapi.org/v2/everything?q=kenya&from=2022-05-03&to=2022-05-01&sortBy=popularity&language=en&apikey=319a22ef8acc48d2a8bc83653dab0ed4'

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)


    return articles_results
    

def process_articles_results(articles_list):
    articles_results = []
    # articles = get_all_articles()
    for article_item in articles_list:
        title = article_item.get('title')
        author = article_item.get('author')
        source = article_item.get('source')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            new_article = Article(title,author,source,description,url,urlToImage,publishedAt)
            articles_results.append(new_article)

    return articles_results

def get_all_sources():
    get_sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=319a22ef8acc48d2a8bc83653dab0ed4'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results

def process_sources_results(sources_list):
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')
        language = source.get('language')

        if name:
            new_source = Sources(id,name,description,url,category,country,language)
            sources_results.append(new_source)

    return sources_results
