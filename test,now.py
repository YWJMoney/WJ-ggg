import pyupbit
import time
import datetime

def cal_target(ticker):                                   
     df = pyupbit.get_ohlcv(ticker, "day", 10)              
     yesterday = df.iloc[-2]                                                         
     yesterday_close = yesterday['close'] *1.03             
     target = yesterday_close                              
     return target

def after_target(ticker):
    df = pyupbit.get_ohlcv(ticker,"day" ,5)
    befor = df.iloc[-2]
    after = befor['close'] *1.0609
    target_sell = after
    return target_sell

def down_target(ticker):                                
    df = pyupbit.get_ohlcv(ticker, "day", 10)              
    yesterday = df.iloc[-2]                                                         
    yesterday_close = yesterday['close'] * 1.03             
    target_down = yesterday_close * 0.985                    
    return target_down
        
def get_ma5(ticker):                                   
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5

access = ""
secret = ""    

upbit = pyupbit.Upbit(access, secret) 
print("autotrade start")                                       

while True:
    now = datetime.datetime.now()                          

    if now: 
        target = cal_target("KRW-BTC")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-BTC")
    target = cal_target("KRW-BTC")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-BTC")
    ma5 = get_ma5("KRW-BTC")
    price = pyupbit.get_current_price("KRW-BTC")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-BTC", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-BTC")     
            upbit.sell_market_order("KRW-BTC", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-QKC")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-QKC")
    target = cal_target("KRW-QKC")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-QKC")
    ma5 = get_ma5("KRW-QKC")
    price = pyupbit.get_current_price("KRW-QKC")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-QKC", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-QKC")     
            upbit.sell_market_order("KRW-QKC", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-SNT")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-SNT")
    target = cal_target("KRW-SNT")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-SNT")
    ma5 = get_ma5("KRW-SNT")
    price = pyupbit.get_current_price("KRW-SNT")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-SNT", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-SNT")     
            upbit.sell_market_order("KRW-SNT", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-THETA")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-THETA")
    target = cal_target("KRW-THETA")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-THETA")
    ma5 = get_ma5("KRW-THETA")
    price = pyupbit.get_current_price("KRW-THETA")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-THETA", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-THETA")     
            upbit.sell_market_order("KRW-THETA", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-EOS")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-EOS")
    target = cal_target("KRW-EOS")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-EOS")
    ma5 = get_ma5("KRW-EOS")
    price = pyupbit.get_current_price("KRW-EOS")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-EOS", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-EOS")     
            upbit.sell_market_order("KRW-EOS", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-FLOW")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-FLOW")
    target = cal_target("KRW-FLOW")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-FLOW")
    ma5 = get_ma5("KRW-FLOW")
    price = pyupbit.get_current_price("KRW-FLOW")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-FLOW", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-FLOW")     
            upbit.sell_market_order("KRW-FLOW", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-BORA")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-BORA")
    target = cal_target("KRW-BORA")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-BORA")
    ma5 = get_ma5("KRW-BORA")
    price = pyupbit.get_current_price("KRW-BORA")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-BORA", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-BORA")     
            upbit.sell_market_order("KRW-BORA", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-HUM")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-HUM")
    target = cal_target("KRW-HUM")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-HUM")
    ma5 = get_ma5("KRW-HUM")
    price = pyupbit.get_current_price("KRW-HUM")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-HUM", krw_balance * 0.05)      
        hold = True                                        

    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-HUM")     
            upbit.sell_market_order("KRW-HUM", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-VET")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-VET")
    target = cal_target("KRW-VET")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-VET")
    ma5 = get_ma5("KRW-VET")
    price = pyupbit.get_current_price("KRW-VET")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-VET", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-VET")     
            upbit.sell_market_order("KRW-VET", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-PUNDIX")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-PUNDIX")
    target = cal_target("KRW-PUNDIX")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-PUNDIX")
    ma5 = get_ma5("KRW-PUNDIX")
    price = pyupbit.get_current_price("KRW-PUNDIX")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-PUNDIX", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-PUNDIX")     
            upbit.sell_market_order("KRW-PUNDIX", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-AAVE")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-AAVE")
    target = cal_target("KRW-AAVE")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-AAVE")
    ma5 = get_ma5("KRW-AAVE")
    price = pyupbit.get_current_price("KRW-AAVE")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-AAVE", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-AAVE")     
            upbit.sell_market_order("KRW-AAVE", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-NEO")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-NEO")
    target = cal_target("KRW-NEO")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-NEO")
    ma5 = get_ma5("KRW-NEO")
    price = pyupbit.get_current_price("KRW-NEO")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-NEO", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-NEO")     
            upbit.sell_market_order("KRW-NEO", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-LOOM")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-LOOM")
    target = cal_target("KRW-LOOM")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-LOOM")
    ma5 = get_ma5("KRW-LOOM")
    price = pyupbit.get_current_price("KRW-LOOM")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-LOOM", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-LOOM")     
            upbit.sell_market_order("KRW-LOOM", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-ICX")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-ICX")
    target = cal_target("KRW-ICX")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-ICX")
    ma5 = get_ma5("KRW-ICX")
    price = pyupbit.get_current_price("KRW-ICX")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-ICX", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-ICX")     
            upbit.sell_market_order("KRW-ICX", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-AVAX")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-AVAX")
    target = cal_target("KRW-AVAX")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-AVAX")
    ma5 = get_ma5("KRW-AVAX")
    price = pyupbit.get_current_price("KRW-AVAX")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-AVAX", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-AVAX")     
            upbit.sell_market_order("KRW-AVAX", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-JST")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-JST")
    target = cal_target("KRW-JST")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-JST")
    ma5 = get_ma5("KRW-JST")
    price = pyupbit.get_current_price("KRW-JST")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-JST", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-JST")     
            upbit.sell_market_order("KRW-JST", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    if now: 
        target = cal_target("KRW-ATOM")                     
        op_mode = True                                  
    
    target_down = down_target("KRW-ATOM")
    target = cal_target("KRW-ATOM")                     
    op_mode = False                                                        
    hold = False    
    target_sell = after_target("KRW-ATOM")
    ma5 = get_ma5("KRW-ATOM")
    price = pyupbit.get_current_price("KRW-ATOM")            

    if op_mode is True and  price is not None and price and ma5 >= target and hold is False: 
        krw_balance = upbit.get_balance("KRW")             
        upbit.buy_market_order("KRW-ATOM", krw_balance * 0.05)      
        hold = True                                        

        # 매도 시도
    if now:
        if op_mode is True and hold is True and target_sell >= price or target_down <= price:       
            balance = upbit.get_balance("KRW-ATOM")     
            upbit.sell_market_order("KRW-ATOM", balance * 0.9995) 
            hold = False                                    
    # 상태 출력
    # print(f"현재시간: {now} 구매가: {target} 목표가: {target_sell}  현재가: {price} 손절가: {target_down} 보유형태: {hold} 동작상태: {op_mode}")

    time.sleep(1)                                      
