class MoviesFilter:

  def __init__(self, filters, movies):
    self.filters = filters
    self.movies = movies

  def apply(self):
    return filter(self.__apply_filter_to_movie, self.movies)

  def __apply_filter_to_movie(self, movie):
    result = True

    for filter_name in self.filters:
      if self.filters[filter_name]:
        filter_func = getattr(self, filter_name)
        result = result and filter_func(movie, self.filters[filter_name])

    return result

  def rating_gt(self, movie, value):
    return movie.rating > value

  def rating_lt(self, movie, value):
    return movie.rating < value

  def year_gt(self, movie, value):
    return movie.year > value

  def year_lt(self, movie, value):
    return movie.year < value
