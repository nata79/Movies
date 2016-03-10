from tabulate import tabulate

class TableFormatter:
  HEADERS = ["Title", "Year", "IMDB Rating", "IMDB URL"]

  def __init__(self, movies):
    self.movies = movies

  def format(self):
    return tabulate(map(self.__to_list, self.movies), headers=TableFormatter.HEADERS, tablefmt="psql")

  def __to_list(self, movie):
    return [movie.title, movie.year, movie.rating, movie.imdb_url]
