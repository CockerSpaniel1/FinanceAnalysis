# 取得資料 dictionary 格式
from myfunc import *
kbar = getStockDaily_dict( '0050' )

# 指標計算
from talib.abstract import *
rsi_short_period=20
rsi_long_period=120
short_rsi=RSI(kbar,timeperiod=rsi_short_period)
long_rsi=RSI(kbar,timeperiod=rsi_long_period)

# 策略判斷
trade_record=[]
index = 0
for i in range(rsi_long_period+1,len(kbar['time'])-1):
    # 進出場時間
    c_time = kbar['time'][i]
    c_close = kbar['close'][i]
    n_time = kbar['time'][i+1]
    n_open = kbar['open'][i+1]
    # rsi
    c_short_rsi = short_rsi[i]
    c_long_rsi = long_rsi[i]
    # 部位空手
    if index == 0:
        # RSI 跌入超賣區
        if c_short_rsi - c_long_rsi <= -10:
            index = 1
            order_time = n_time
            order_price = n_open
            continue
    elif index == 1:
        # RSI 漲回超買區
        if c_short_rsi >= c_long_rsi:
            index = 0 
            cover_time = n_time
            cover_price = n_open
            trade_record.append(['B',order_time,order_price,cover_time,cover_price])
            print('買進 時間: %s 價格: %s 出場 時間: %s 價格: %s' %(order_time,order_price,cover_time,cover_price) )
            
# 計算績效指標 
getPerformance(trade_record)

# 繪製 Ma 及下單圖
import mplfinance as mpf
addp1=[]
# 把 ma的畫圖物件 丟到 下單紀錄的圖表內 
chartOrder(kbar,trade_record,addp1)