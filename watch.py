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

    print ("Adding " + symbol + " ($" + str(price) + ")" + " to watchlist...")
    watchlist[symbol] = price

print "Startup configuration complete.\n"


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
        trading_price = float(q['last_trade_price'])
        threshold_price = float(watchlist[q['symbol']])

        if trading_price <= threshold_price:
            print q['symbol'], ": ", trading_price
    print "Finished fetching quotes.\n"

while True:
    run_routine()
    time.sleep(60)