# Movies

This is a CLI application that cross references data from IMDB and Netflix to provide movie suggestions.

## Usage

```
python movies.py imdb top250 --year_gt 2000 --year_lt 2010 --rating_gt 8.2
```

## Status

Currently the only implemented feature fetches the top 250 IMDB list and filters the titles that are not available on Netflix.
