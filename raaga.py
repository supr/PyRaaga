import re
import os
from HTTPOpener import HTTPOpener
from metadata import Track

class Raaga(object):
    def __init__(self, opener=None, lang="telugu"):
        self.opener = opener if opener else HTTPOpener()
        self.lang = lang
        
    def get_movie_ids(self):
        URL = "http://www.raaga.com/channels/%s/movies.asp"%(self.lang)
        movie_list = self.opener.open(URL).read()
        rx = "\"sAI\(this, \'(.*?)\'\);\""
        return [ id.strip() for id in re.findall(rx,movie_list)]

    def _get_movie_track_title(self, page):
        rx_track_list = "class=\"contentSubHead\" title=\"(.*?)\""
        return [ title.strip() for title in re.findall(rx_track_list, page) ]
                 
    def get_movie_info(self, movie_id):
        URL = "http://www.raaga.com/channels/%s/moviedetail.asp?mid=%s"%(self.lang, movie_id)
        movie_detail = self.opener.open(URL).read()
        return self._get_movie_track_title(movie_detail)   

if __name__ == "__main__":
    os.path.join(os.path.abspath(os.path.dirname(__file__)))
    raaga = Raaga()
    movie_ids = raaga.get_movie_ids()
    print "Total Movie IDs fetched: ", len(movie_ids)
