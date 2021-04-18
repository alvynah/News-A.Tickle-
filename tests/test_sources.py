import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources("usa-today", "USA Today", "Get the latest national, international, and political news at USATODAY.com.",
                                  "http://www.usatoday.com/news", "general", "en", "us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))


if __name__ == '__main__':
    unittest.main()
