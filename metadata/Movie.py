class Movie(object):
    def __init__(self,name,tracks = [], raaga_id = None):
        self.name = name
        self.tracks = tracks
        self.raaga_id = raaga_id
    
    def set_tracks(self, tracks):
        self.tracks = tracks

    def set_raaga_id(self, raaga_id):
        self.raaga_id = raaga_id

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __eq__(self, other):
        if(isinstance(other, Movie)):
            return ((self.name == other.name) and (self.tracks == other.tracks)
                    and (self.raaga_id == other.raaga_id))
        else:
            return False
