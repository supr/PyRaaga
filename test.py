import unittest
from raaga import Raaga
from metadata.Track import Track
from metadata.Movie import Movie

class RaagaTestCase(unittest.TestCase):
    def setUp(self):
        self.raaga = Raaga()
        
    def testGetMovieIds(self):
        self.assertNotEqual(self.raaga.get_movie_ids(), [])

    def testGetMovieInfo(self):
        t1 = Track("Anandha Ragam")
        t1.set_artists(['Susheela'])
        t1.set_music(['Illayaraja'])
        t2 = Track("Navvulalona")
        t2.set_artists(['SP. Balasubramaniam','Janaki'])
        t2.set_music(['Illayaraja'])
        m = Movie("Madhura Geetham", [t1,t2])
        self.assertEqual(self.raaga.get_movie_info('A0002038'), m)
        
if __name__ == "__main__":
    unittest.main()
