import os.path
import json
import progressbar
from lib.clients.netflix import NetflixSession, NetflixClient
from lib.clients.imdb import ImdbClient
from lib.models.movie import Movie
from lib.formatters.table_formatter import TableFormatter
from lib.movies_filter import MoviesFilter

class MoviesApp:

  def __init__(self):
    if os.path.isfile('netflix.cookies'):
      with open('netflix.cookies', 'r') as f:
        self.netflix_session = NetflixSession.restore(json.loads(f.read()))
    else:
      email = os.environ['NETFLIX_EMAIL']
      password = os.environ['NETFLIX_PASSWORD']

      self.netflix_session = NetflixSession.new(email, password)

      with open('netflix.cookies', 'w') as f:
        f.write(json.dumps(self.netflix_session.cookies))

    self.netflix_client = NetflixClient(self.netflix_session)
    self.imdb_client = ImdbClient()

  def imdb_top250(self, filters):
    bar = progressbar.ProgressBar()

    movies = self.imdb_client.get_top_250_movies()
    movies = list(MoviesFilter(filters, movies).apply())
    movies = self.netflix_client.filter_available_movies(bar(movies))

    return TableFormatter(movies).format()
