# Magnr-coin
 crypto coin data ingestion and REST API

## Description
 This is a two part function of a streaming cryptocurrency application with python. This project uses a websocket stream api from *wss://ws-feed.exchange.coinbase.com* by using a ticker stream. The coins that are streamed are:

- Bitcoin (BTC)
- Ethereum (ETH)
- Cardano (ADA)
- Solana (SOL)
- Polkadot (DOT)
- Litecoin (LTC)
- Polygon (MATIC)
- Chainlink (LINK)
- Tezos (XTZ)

The streamed data are persisted in a database (sqlite3) and can be serve (the data) using the REST API created


## Requirements

1. Python packages
 - the list of packages used can be found in the *requirements.txt*. To install it, execute thefollowing command on the power shell:
 ``` 
pip install -r requirements.txt
 ``` 

## How to use
1. Data ingestion
 - the data ingestion process can be execute by running the *coinIngest.py* file:
 ```
python coinStream.py
 ```

 2. Data Serving
 - the data serving process in the form of REST API can be execute by running the *coinServe.py* file:
 ```
python coinServe.py
 ```

