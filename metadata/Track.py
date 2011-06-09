class Track(object):
    def __init__(self, title):
        self.title = title

    def set_artists(self, artists=[]):
        self.artists = artists

    def set_lyricist(self, lyricist=None):
        self.lyricist = lyricist

    def __dict__(self):
        return dict(
            Title = self.title,
            Artists = self.artists,
            Lyricist = self.lyricist
            )
