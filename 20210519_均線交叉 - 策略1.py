from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
short_sma=SMA(kbar,timeperiod=5)
long_sma=SMA(kbar,timeperiod=60)


index = 0   
for i in range(60+1, len(kbar["time"])):
    c_time = kbar['time'][i]
    n_time = kbar['time'][i+1]
    n_open = kbar['open']
        
    last_s_ma = short_sma[i-1]
    last_l_ma = long_sma[i-1]
    
    c_s_ma = short_sma[i]
    c_l_ma = long_sma[i]
    
    
    if index == 0:
        if last_s_ma <= last_l_ma and c_s_ma > c_l_ma:
            index = 1
            order_time = n_time
            order_price = n_open
            continue
    elif index == 1:        
        if last_s_ma >= last_l_ma and c_s_ma < c_l_ma:    
            index = 0
            cover_time = n_time
            cover_price = n_open
            
            print("買進 時間: %s 價格: %s 出場 時間: %s 價格: %s" %(order_time, order_price, cover_time, cover_price ))
            