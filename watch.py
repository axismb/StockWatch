import requests
import urllib2

__author__ = 'Aziz Batihk'

# get quote of specified symbols
def get_quote(symbols):
    url = "https://api.robinhood.com/quotes/"
    query = { 'symbols': symbols }
    resp = requests.session().get(url, params=query)
    resp = resp.json()
    return resp['results']

# main check
def do_routine():

# read stocks file
stock_file = "stock.txt"
lines = open(stock_file).read().splitlines()

# init watchlist
watchlist = {}

# add each stock from config
for l in lines:
    res = l.split()
    symbol = res[0].upper()
    price = float(res[1])

    print ("Adding " + symbol + " to watchlist...")
    watchlist[symbol] = price

