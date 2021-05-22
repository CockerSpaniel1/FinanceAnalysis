from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
long_sma=SMA(kbar,timeperiod=60)    # 前59筆是空值

# 交易紀錄的物件
trade_record=[]
# 儲存目前部位的變數
index=0
# 回測的方式 
for i in range(60,len(kbar['time'])-1):
    c_time=kbar['time'][i]
    c_close=kbar['close'][i]
    last_20_high=max(kbar['high'][i-20:i])
    last_20_low=min(kbar['low'][i-20:i])
    n_open=kbar['open'][i+1]
    n_time=kbar['time'][i+1]
    # 取得 MA
    c_sma=long_sma[i]
    
    # 當目前部位空手 收盤價 大於前20日的最高價 買進
    # 並且小於 60 ma
    if index == 0 and c_close > last_20_high and c_close < c_sma:
        # 買進
        index = 1
        order_time = n_time
        order_price = n_open
        # 停損點
        stop_loss = round((last_20_high + last_20_low )/2)
        # 停損的點數
        stop_loss_number = order_price - stop_loss
        continue
    # 如果目前部位是多方 
    elif index == 1:
        # 如果收盤價減去停損點數 大於 停損價位 則 上修停損價位 
        if c_close - stop_loss_number >= stop_loss:
            stop_loss = c_close - stop_loss_number
        # 收盤價 小於 停損點  ( 當漲幅 大於 停損的點數 這時候觸發到停損時 會是獲利的 )
        elif c_close <= stop_loss:
            index = 0 
            cover_time = n_time
            cover_price = n_open
            print('進場時間:%s 進場價格:%s 出場時間:%s 出場價格:%s' % (order_time,order_price,cover_time,cover_price))
            # 加入交易紀錄
            trade_record.append(['B',order_time,order_price,cover_time,cover_price])
            continue
        
# 計算績效指標 
getPerformance(trade_record)
    
# 繪製 Ma 及下單圖
import mplfinance as mpf
addp1=[]
addp1.append(mpf.make_addplot(long_sma,color='#CC0000'))
chartOrder(kbar,trade_record,addp1)




