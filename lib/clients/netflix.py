import urllib.request
import requests
import json
from lxml import html
from lib.models.movie import Movie

class NetflixSession:

  @classmethod
  def new(klass, email, password):
    provisional_cookies = klass.__get_provisional_cookies()
    auth_url = klass.__get_auth_url()
    cookies = klass.__login(provisional_cookies, auth_url, email, password)
    return klass(cookies)

  @classmethod
  def __get_provisional_cookies(klass):
    url = "https://www.netflix.com"
    response = requests.get(url, allow_redirects=False)
    return response.cookies.get_dict()

  @classmethod
  def __get_auth_url(klass):
    url = "https://www.netflix.com/Login"
    response = requests.get(url)
    tree = html.fromstring(response.content)
    return tree.xpath('//input[@name="authURL"]')[0].value

  @classmethod
  def __login(klass, provisional_cookies, auth_url, email, password):
    url = "https://www.netflix.com/Login?locale=en-GB"

    data = {
      'authURL': auth_url,
      'email': email,
      'password': password,
      'RememberMe': 'on'
    }

    response = requests.post(url, data=data, cookies=provisional_cookies,
      allow_redirects=False)

    return {
      'NetflixId': response.cookies['NetflixId'],
      'SecureNetflixId': response.cookies['SecureNetflixId']
    }

  @classmethod
  def restore(klass, cookies):
    return klass(cookies)

  def __init__(self, cookies):
    self.cookies = cookies

class NetflixClient:
  HOST = 'https://api-global.netflix.com/'

  def __init__(self, session):
    self.session = session

  def filter_available_movies(self, movies):
    return filter(self.is_movie_available, movies)

  def is_movie_available(self, movie):
    path = urllib.request.pathname2url('["search","videos","{}","1"]'.format(movie.title))
    url = "{host}iosui/search/0.2?country=GB&path={path}".format(
      host=NetflixClient.HOST, path=path)

    json = requests.get(url, cookies=self.session.cookies).json()
    return 'videos' in json['value']['search']['videos'][movie.title]['1']
