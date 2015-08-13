import requests
import urllib2
import time

__author__ = 'Aziz Batihk'

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


# get quote of specified symbols
def get_quote(symbols):
    url = "https://api.robinhood.com/quotes/?symbols="
    resp = requests.session().get(url + ",".join(symbols) )
    resp = resp.json()
    return resp['results']

# run main
def run_routine():
    print ("Getting quotes...")
    quotes = get_quote(watchlist.keys())

    for q in quotes:
        if q['last_trade_price'] <= watchlist[q['symbol']]:
            print q['symbol'], ": ", q['last_trade_price']

while True:
    run_routine()
    time.sleep(60)