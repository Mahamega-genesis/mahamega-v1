import requests
import time
import hmac
import hashlib

API_KEY = 'gV8r7HVtX3h6xfyRwC'
API_SECRET = 'NdJqLbgW4WD3FQKUd4ery0iG5v5vaDL06taO'
BASE_URL = "https://api.bybit.com"

def get_signature(params, secret):
    param_str = '&'.join([f"{k}={v}" for k, v in sorted(params.items())])
    return hmac.new(bytes(secret, "utf-8"), bytes(param_str, "utf-8"), hashlib.sha256).hexdigest()

def fetch_price_data(coin):
    symbol_map = {
        "bitcoin": "BTCUSDT",
        "ethereum": "ETHUSDT",
        "solana": "SOLUSDT",
        "ripple": "XRPUSDT",
        "dogecoin": "DOGEUSDT"
    }

    symbol = symbol_map.get(coin.lower())
    if not symbol:
        raise ValueError(f"Coin {coin} not supported")

    endpoint = "/v2/public/kline/list"
    params = {
        "symbol": symbol,
        "interval": "1",   # 1-minute candle
        "limit": 100
    }

    response = requests.get(BASE_URL + endpoint, params=params)
    data = response.json()

    if data['ret_code'] != 0:
        raise Exception(f"Bybit API error: {data}")

    # Ambil data harga close dan time
    price_data = [{
        'timestamp': int(candle[0]),
        'open': float(candle[1]),
        'high': float(candle[2]),
        'low': float(candle[3]),
        'close': float(candle[4]),
        'volume': float(candle[5])
    } for candle in data['result']]

    return price_data
