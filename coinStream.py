import websocket, json, sqlite3
import os.path as path
import dateutil.parser as dp

def init_db():
    conn = sqlite3.Connection('coins.db')
    cur = conn.cursor()
    coins = ['BTCUSD', 'ETHUSD', 'ADAUSD', 'SOLUSD','DOTUSD', 'LTCUSD', 'MATICUSD', 'LINKUSD', 'XTZUSD']
    
    for c in coins:
        
        statemt = """CREATE TABLE {}(
            sequence int,
            product_id text,
            price float,
            volume_24h float,
            side text,
            time int,
            last_size float
            )""".format(c)
        
        cur.execute(statemt)
        conn.commit()
    
    conn.close()

def cointodb(message):
    conn = sqlite3.Connection('coins.db')
    cur = conn.cursor()
    obj = json.loads(message)
    
    del obj['type']
    del obj['open_24h']
    del obj['low_24h']
    del obj['high_24h']
    del obj['volume_30d']
    del obj['best_bid']
    del obj['best_ask']
    del obj['trade_id']
    
    tname = obj['product_id'].replace("-", "")
    stmt = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?)".format(tname)
    time = int(dp.parse(obj['time']).timestamp())
    obj['time'] = time
    par = list(obj.values())

    
    cur.execute(stmt, par)
    conn.commit()
    conn.close()
    
    

def on_open(ws):
    print('##OPENED##')
    subscribe_mesage = {
        'type':'subscribe',
        'channels': [
            {
                'name':'ticker',
                'product_ids':['BTC-USD',
                               'ETH-USD',
                               'ADA-USD',
                               'SOL-USD',
                               'DOT-USD',
                               'LTC-USD',
                               'MATIC-USD',
                               'LINK-USD',
                               'XTZ-USD']
            }
        ]
    }
    ws.send(json.dumps(subscribe_mesage))

socket = 'wss://ws-feed.exchange.coinbase.com'

def on_message(ws, message):
    
    if not path.exists("coins.db"):
        init_db()
    
    cointodb(message)
    
def on_close(ws):
    print("##CLOSED##")

ws = websocket.WebSocketApp(socket, on_open=on_open,
                             on_message=on_message,
                             on_close=on_close)

ws.run_forever()