from api import api
from .controllers import OneMovie, MovieList

api.add_resource(OneMovie, '/movie')
api.add_resource(MovieList, '/movie/all')