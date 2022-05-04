import unittest
from models import Article

class article_test(unittest.TestCase):
    '''
    testing the behavior of class articles
    '''
    def setUp(self):
        self.new_article = Article("bbc-news", "Justine Calma", "Why fossil fuel companies see green in Bitcoin mining projects", "ExxonMobil and other fossil fuel companies have turned to Bitcoin mining to address a gas problem. But their plans come with risks.",  "https://www.theverge.com/2022/5/4/23055761/exxonmobil-cryptomining-bitcoin-methane-gas", "https://cdn.vox-cdn.com/thumbor/BZdljrBbt8tBl6oCCnckcDKqe6g=/0x90:4608x2503/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23435975/1240300988.jpg", "https://cdn.vox-cdn.com/thumbor/BZdljrBbt8tBl6oCCnckcDKqe6g=/0x90:4608x2503/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23435975/1240300988.jpg",)

    def test_instance(self):
     self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()