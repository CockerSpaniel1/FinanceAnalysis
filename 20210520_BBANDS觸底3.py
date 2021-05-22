from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
upper,middle,lower=BBANDS(kbar,timeperiod=20)

# 交易紀錄的物件
trade_record=[]
# 移動停損比率
stop_ratio=0.05

index = 0
for i in range(20+1,len(kbar['time'])-1):
    # 進出場時間
    l_close = kbar['close'][i-1]
    
    c_time = kbar['time'][i]
    c_close = kbar['close'][i]
    c_open = kbar['open'][i]
    n_time = kbar['time'][i+1]
    n_open = kbar['open'][i+1]
    
    c_lower=lower[i]
    c_upper=upper[i]
    
    # 部位空手
    if index == 0:
        # ma 向上交叉的判斷 # 跳空缺口 今日的開盤 比 昨日的開盤 低 n% 
        if c_open < c_lower and c_open <= l_close * 0.97 :
            index = 1
            order_time = c_time
            order_price = c_open
            # stop_loss = order_price * (1-stop_ratio)
            continue
    elif index == 1:
        # 如果 收盤價乘上停損比率 大於 停損點
        # if c_close * (1-stop_ratio) >= stop_loss:
            # stop_loss = c_close * (1-stop_ratio)
        # if c_close <= stop_loss:
            # index = 0 
            # cover_time = n_time
            # cover_price = n_open
            # trade_record.append(['B',order_time,order_price,cover_time,cover_price])
            # print('買進 時間: %s 價格: %s 出場 時間: %s 價格: %s' %(order_time,order_price,cover_time,cover_price))
        if c_close >= c_upper:
            index = 0 
            cover_time = n_time
            cover_price = n_open
            trade_record.append(['B',order_time,order_price,cover_time,cover_price])
            print('買進 時間: %s 價格: %s 出場 時間: %s 價格: %s' %(order_time,order_price,cover_time,cover_price))
            
# 計算績效指標 
getPerformance(trade_record)

# 繪製 Ma 及下單圖
import mplfinance as mpf
addp1=[]
addp1.append(mpf.make_addplot(upper))
addp1.append(mpf.make_addplot(middle))
addp1.append(mpf.make_addplot(lower))
# 把 ma的畫圖物件 丟到 下單紀錄的圖表內 
chartOrder(kbar,trade_record,addp1)