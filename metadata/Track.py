class Track(object):
    def __init__(self, title, artists=[], lyricist=None, music=None):
        self.title = title
        self.artists = artists
        self.lyricist = lyricist
        self.music = music

    def set_artists(self, artists=[]):
        self.artists = artists

    def set_lyricist(self, lyricist=None):
        self.lyricist = lyricist

    def set_music(self, music=None):
        self.music = music

    def __dict__(self):
        return dict(
            Title = self.title,
            Artists = self.artists,
            Lyricist = self.lyricist,
            Music = self.music,
            )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def __eq__(self, other):
        if(isinstance(other, Track)):
            return ((self.title == other.title) and (self.artists == other.artists) 
                    and (self.lyricist == other.lyricist) and (self.music == other.music))
        else:
            return False
