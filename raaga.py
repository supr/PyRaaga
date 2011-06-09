import re
import os
from lxml import etree
from HTTPOpener import HTTPOpener
from metadata.Track import Track
from metadata.Movie import Movie

class Raaga(object):
    def __init__(self, opener=None, lang="telugu"):
        self.opener = opener if opener else HTTPOpener()
        self.lang = lang
        
    def get_movie_ids(self):
        URL = "http://www.raaga.com/channels/%s/movies.asp"%(self.lang)
        movie_list = self.opener.open(URL).read()
        rx = "\"sAI\(this, \'(.*?)\'\);\""
        return [ id.strip() for id in re.findall(rx,movie_list)]

    def _parse_artists(self, desc):
        rx = "<p><\/p><p>Artist\(s\): (.*?)<br\/>Music: (.*?)<br\/><\/p>"
        m = re.search(rx, desc)
        artists, music_director = m.groups()
        artists = [ a.strip() for a in artists.split(",") ]
        music_director = [ m.strip() for m in music_director.split(",")]
        return [artists, music_director]

    def _parse_movie_title(self, titlestr):
        rx = "Raaga.com - (.*) Telugu songs"
        m = re.search(rx, titlestr)
        return m.group(1)

    def get_movie_info(self, movie_id):
        URL = "http://www.raaga.com/a/rss.asp?%s"%(movie_id)
        rss = "".join([ line.strip() for line in self.opener.open(URL).readlines() ])
        
        mi_tree = etree.fromstring(rss)
        mi_title = self._parse_movie_title(mi_tree.xpath("/rss/channel/title/text()")[0])
        mi_tracks = mi_tree.xpath("/rss/channel/item")
        tracks = []
        for mi_track in mi_tracks:
            track_title = mi_track.xpath("title/text()")[0]
            track_desc = mi_track.xpath("description/text()")[0]
            track_info = self._parse_artists(track_desc)
            track = Track(track_title)
            track.set_artists(track_info[0])
            track.set_music(track_info[1])
            tracks.append(track)
        return Movie(mi_title, tracks)
