from json import JSONEncoder
from metadata.Movie import Movie
from metadata.Track import Track

class MetadataJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Movie) or isinstance(obj, Track):
            return obj.__dict__
        return JSONEncoder.default(self, obj)
