import click
from lib.movies_app import MoviesApp

app = MoviesApp()

def filterable_command(fn):
  decorators = [
    click.option('--year_gt', type=int),
    click.option('--year_lt', type=int),
    click.option('--rating_gt', type=float),
    click.option('--rating_lt', type=float),
    click.command()
  ]

  command = fn

  for decorator in decorators:
      command = decorator(command)

  return command

@click.group()
def cli():
  pass

@click.group()
def imdb():
  pass

@filterable_command
def top250(**filters):
  """IMDB top 250 titles available on Netflix"""
  click.echo(app.imdb_top250(filters))

cli.add_command(imdb)
imdb.add_command(top250)

cli()
