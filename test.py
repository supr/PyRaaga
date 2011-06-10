import unittest
from json import dumps
from raaga import Raaga
from metadata.Track import Track
from metadata.Movie import Movie
from encoder.MetadataEncoder import MetadataJSONEncoder

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.raaga = Raaga()
        track1 = Track("Anandha Ragam")
        track1.set_artists(['Susheela'])
        track1.set_music(['Illayaraja'])
        track2 = Track("Navvulalona")
        track2.set_artists(['SP. Balasubramaniam', 'Janaki'])
        track2.set_music(['Illayaraja'])
        self.movie = Movie("Madhura Geetham", [track1, track2])

class RaagaTestCase(BaseTestCase):
    def testGetMovieIds(self):
        self.assertNotEqual(self.raaga.get_movie_ids(), [])

    def testGetMovieInfo(self):
        self.assertEqual(self.raaga.get_movie_info('A0002038'), self.movie)
        
class MetadataJSONEncoderTestCase(BaseTestCase):
    def test_default(self):
        jstr = '{"tracks": [{"lyricist": null, "artists": ["Susheela"], "music": ["Illayaraja"], "title": "Anandha Ragam"},\
 {"lyricist": null, "artists": ["SP. Balasubramaniam", "Janaki"],\
 "music": ["Illayaraja"], "title": "Navvulalona"}], "name": "Madhura Geetham"}'
        mjs = dumps(self.movie, cls = MetadataJSONEncoder)
        self.assertEqual(mjs, jstr)

if __name__ == "__main__":
    unittest.main()
