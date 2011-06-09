import unittest
from raaga import Raaga

class RaagaTestCase(unittest.TestCase):
    def setUp(self):
        self.raaga = Raaga()
        
    def testGetMovieIds(self):
        self.assertNotEqual(self.raaga.get_movie_ids(), [])

    def testGetMovieInfo(self):
        self.assertEqual(self.raaga.get_movie_info('A0002038'), ['Anandha Ragam','Navvulalona'])
        self.assertEqual(self.raaga.get_movie_info('A0002039'), ['Koru Kunnaanu',])
        
if __name__ == "__main__":
    unittest.main()
