import pyupbit
import time

def target_price(ticker):                                  
    df = pyupbit.get_ohlcv(ticker,"day", 10)
    today = df.iloc[-1]
    target = today['open'] * 1.015
    return target

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker,"day", 10)
    today = df.iloc[-1]
    good_target = today['open'] * 1.0404
    return good_target

def current_price(ticker):                                 
    price = pyupbit.get_current_price(ticker)
    return price

def dum_price(ticker):
    df = pyupbit.get_current_price(ticker)
    dump_price = df *0.985
    return dump_price

def get_ma5(ticker):                                   
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

tickers = [
    'KRW-QKC',
    'KRW-SNT',
    'KRW-THETA',
    'KRW-EOS',
    'KRW-FLOW',
    'KRW-BORA',
    'KRW-HUM',
    'KRW-VET',
    'KRW-PUNDIX',
    'KRW-AAVE',
    'KRW-NEO',
    'KRW-LOOM',
    'KRW-ICX',
    'KRW-AVAX',
    'KRW-JST',
    'KRW-ATOM',
    'KRW-BTC'
    ]

access = ""
secret = ""         

upbit = pyupbit.Upbit(access, secret) 

free = False

while True:

    for a in tickers: 
        target = target_price(a)
        price = current_price(a)
        dump_price = dum_price(a)
        good_target = get_target_price(a)

        while price >= target and free is False and price and good_target > price:
            krw = upbit.get_balance("KRW")
            upbit.buy_market_order(a, krw * 0.05) 
            free = True

            if price >= good_target and free is True:
                coin = upbit.get_balance(a)
                upbit.sell_market_order(a, coin * 0.9995)
                free = False

            if dump_price >= price and free is True:
                coin = upbit.get_balance(a)
                upbit.sell_market_order(a, coin * 0.9995)
                free = False

    time.sleep(1)



     
