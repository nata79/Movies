import requests
from lxml import html
from lib.models.movie import Movie

class ImdbClient:

  def get_top_250_movies(self):
    response = requests.get('http://www.imdb.com/chart/top')
    tree = html.fromstring(response.content)

    movies = []

    for element in tree.xpath('//tbody[@class="lister-list"]//tr'):
      name = element.xpath('td[@class="titleColumn"]/a/text()')[0]
      year = element.xpath('td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()')[0].replace('(', '').replace(')', '')
      rating = element.xpath('td[@class="ratingColumn imdbRating"]/strong/text()')[0]
      imdb_url = element.xpath('td[@class="titleColumn"]/a/@href')[0]

      movies.append(Movie(name, year, rating, imdb_url))

    return movies
