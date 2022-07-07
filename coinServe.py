from distutils.log import debug
from flask import Flask, request
import sqlite3

app = Flask(__name__)

#Endpoint 1
#Get the current price of an asset (coin)
#/price/{symbol}
@app.route("/price/<symbol>")
def coinPrice(symbol):

    conn = sqlite3.connect('coins.db')
    cur = conn.cursor()
    stmt = "SELECT price FROM {symbol}USD ORDER BY time DESC LIMIT 1".format(symbol=symbol)
    cur.execute(stmt)
    obj = cur.fetchone()[0]
    
    return {'price': str(obj)}

#Endpoint 2
#Get the price of a coin in a given timeframe 
#/graph/{symbol}?start=12345678&end=12345678
@app.route("/graph/<symbol>")
def coinTPrice(symbol):
    
    start = request.args.get('start')
    end = request.args.get('end')
    conn = sqlite3.connect('coins.db')
    cur = conn.cursor()
    stmt = "SELECT price FROM {symbol}USD WHERE time BETWEEN {start} AND {end} LIMIT 1".format(symbol=symbol, start=start, end=end)
    cur.execute(stmt)
    obj = cur.fetchone()[0]
    
    return {'price': str(obj)}


#Endpoint 3 
#Get the volume of an asset
@app.route("/info/volume/<symbol>")
def coinVolume(symbol):

    conn = sqlite3.connect('coins.db')
    cur = conn.cursor()
    stmt = "SELECT volume_24h FROM {symbol}USD ORDER BY time DESC LIMIT 1".format(symbol=symbol)
    cur.execute(stmt)
    obj = cur.fetchone()[0]
    
    return {'volume': str(obj)}

#Endpoint 4
#Get the size of a chain 
@app.route("/info/size/<symbol>")
def coinSize(symbol):

    conn = sqlite3.connect('coins.db')
    cur = conn.cursor()
    stmt = "SELECT volume_24h FROM {symbol}USD ORDER BY time DESC LIMIT 1".format(symbol=symbol)
    cur.execute(stmt)
    obj = cur.fetchone()[0]
    
    return {'size': str(obj)}

if __name__ == "__main__":
    app.run(debug=True)