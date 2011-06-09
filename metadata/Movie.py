class Movie(object):
    def __init__(self,name,tracks = []):
        self.name = name
        self.tracks = tracks
    
    def set_tracks(self, tracks):
        self.tracks = tracks

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __eq__(self, other):
        if(isinstance(other, Movie)):
            "Matching names",self.name == other.name,"Matching Tracks", self.tracks == other.tracks
            return ((self.name == other.name) and (self.tracks == other.tracks))
        else:
            return False
