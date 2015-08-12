import requests
import urllib2

__author__ = 'Aziz Batihk'


def get_quote(symbols):
    url = "https://api.robinhood.com/quotes/"
    query = { 'symbols': symbols }
    resp = requests.session().get(url, params=query)
    resp = resp.json()
    return resp['results']
