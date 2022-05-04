import unittest
from models import news

class news_test(unittest.TestCase):
    '''
    testing the behavior of class news
    '''
    def setUp(self):
        self.new_article = Articles("Marca", "Marca W", "US Family Claims Someone Used Apple AirTag To Track Them At Disney World")
        return 