import unittest
from models import Sources

class sources_test(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",  "https://abcnews.go.com", "general",  "en", "us" )

    def test_instance(self):
     self.assertTrue(isinstance(self.new_source, Sources))

if __name__ == '__main__':
    unittest.main()