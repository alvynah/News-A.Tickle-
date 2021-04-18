import unittest
from app.models import Articles


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles("abc-news", "ZEKE MILLER, AAMER MADHANI and JULIE WATSON Associated Press", "After outcry, Biden plans to lift refugee cap in May", "After outcry, Pres. Biden plans to lift the refugee cap in May.", "https://abcnews.go.com/Politics/wireStory/outcry-biden-plans-lift-refugee-cap-77147056",
                                    "https://s.abcnews.com/images/Politics/WireAP_af5e476b20204daa83d9b6e02fe738f7_16x9_992.jpg", "2021-04-18T09:11:02Z", "WASHINGTON -- President Joe Biden plans to lift his predecessors historically low cap on refugees by next month, after initially moving only to expand the eligibility criteria for resettlements and g… [+5806 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))


