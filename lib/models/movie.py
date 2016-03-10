class Movie:

  def __init__(self, title, year, rating, imdb_url):
    self.title = title
    self.year = int(year)
    self.rating = float(rating)
    self.imdb_url = 'http://www.imdb.com/' + imdb_url.split('?')[0]
