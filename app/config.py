
class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2'
    NEWS_API_KEY = '4a6f270476a3464092781657cfcaa274'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(NEWS_API_KEY)
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    
    pass


class ProdConfig(Config):
    
    pass


class DevConfig(Config):
    

    DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }