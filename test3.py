import pyupbit

def target_price(ticker):                                  
    df = pyupbit.get_ohlcv(ticker,"day", 10)
    today = df.iloc[-1]
    target = today['open'] * 1.01
    return target

def get_target_price(ticker):
    df = pyupbit.get_ohlcv(ticker,"day", 10)
    today = df.iloc[-1]
    good_target = today['open'] * 1.04
    return good_target

def current_price(ticker):                                 
    price = pyupbit.get_current_price(ticker)
    return price

def dum_price(ticker):
    target = target_price(ticker)
    dump_price = target * 0.985
    return dump_price

def get_ma5(ticker):                                   
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

tickers = ['KRW-BTC', 'KRW-ETH', 'KRW-NEO', 'KRW-MTL', 'KRW-XRP', 'KRW-ETC', 'KRW-OMG', 'KRW-SNT', 'KRW-WAVES', 'KRW-XEM', 'KRW-QTUM',
 'KRW-LSK', 'KRW-STEEM', 'KRW-XLM', 'KRW-ARDR', 'KRW-ARK', 'KRW-STORJ', 'KRW-GRS', 'KRW-REP', 'KRW-ADA', 'KRW-SBD', 'KRW-POWR', 'KRW-BTG',
  'KRW-ICX', 'KRW-EOS', 'KRW-TRX', 'KRW-SC', 'KRW-ONT', 'KRW-ZIL', 'KRW-POLY', 'KRW-ZRX', 'KRW-LOOM', 'KRW-BCH', 'KRW-BAT', 'KRW-IOST',
   'KRW-RFR', 'KRW-CVC', 'KRW-IQ', 'KRW-IOTA', 'KRW-MFT', 'KRW-ONG', 'KRW-GAS', 'KRW-UPP', 'KRW-ELF', 'KRW-KNC', 'KRW-BSV', 'KRW-THETA',
    'KRW-QKC', 'KRW-BTT', 'KRW-MOC', 'KRW-ENJ', 'KRW-TFUEL', 'KRW-MANA', 'KRW-ANKR', 'KRW-AERGO', 'KRW-ATOM', 'KRW-TT', 'KRW-CRE', 'KRW-MBL',
     'KRW-WAXP', 'KRW-HBAR', 'KRW-MED', 'KRW-MLK', 'KRW-STPT', 'KRW-ORBS', 'KRW-VET', 'KRW-CHZ', 'KRW-STMX', 'KRW-DKA', 'KRW-HIVE', 'KRW-KAVA'
     , 'KRW-AHT', 'KRW-LINK', 'KRW-XTZ', 'KRW-BORA', 'KRW-JST', 'KRW-CRO', 'KRW-TON', 'KRW-SXP', 'KRW-HUNT', 'KRW-PLA', 'KRW-DOT', 'KRW-SRM',
      'KRW-MVL', 'KRW-STRAX', 'KRW-AQT', 'KRW-GLM', 'KRW-SSX', 'KRW-META', 'KRW-FCT2', 'KRW-CBK', 'KRW-SAND', 'KRW-HUM', 'KRW-DOGE', 'KRW-STRK',
       'KRW-PUNDIX', 'KRW-FLOW', 'KRW-DAWN', 'KRW-AXS', 'KRW-STX', 'KRW-XEC', 'KRW-SOL', 'KRW-MATIC', 'KRW-NU', 'KRW-AAVE', 'KRW-1INCH', 'KRW-ALGO',
        'KRW-NEAR', 'KRW-WEMIX', 'KRW-AVAX', 'KRW-T', 'KRW-CELO', 'KRW-GMT', 'KRW-APT']

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
        ma5 =get_ma5(a)

        while price >= target and free is False and price and ma5 <= price and good_target > price:
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

        print(f"코인: {a} 현재가: {price} 구매가: {target} 목표가: {good_target} 손절가: {dump_price} 보유상태: {free}")  




     
