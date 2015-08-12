import requests
import urllib2

__author__ = 'Aziz Batihk'


def get_quote(symbols):
    url = "https://api.robinhood.com/quotes/"
    query = { 'symbols': symbols }
    resp = requests.session().get(url, params=query)
    resp = resp.json()
    return resp['results']

# read stocks file
file = "stock.txt"
lines = open(file).read().splitlines()

# init watchlist
watchlist = {}

# add each stock from config
for l in lines:
    res = l.split()
    symbol = res[0]
    price = float(res[1])

    watchlist[symbol] = price