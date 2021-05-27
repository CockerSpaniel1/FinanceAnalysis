
from talib.abstract import *
short_sma=SMA(kbar,timeperiod=5)    # 前4筆是空值
long_sma=SMA(kbar,timeperiod=60)    # 前59筆是空值

# 交易紀錄的物件
trade_record=[]
# 移動停損比率
stop_ratio=0.05

index = 0
for i in range(60+1,len(kbar['time'])-1):
    # 進出場時間
    c_time = kbar['time'][i]
    c_close = kbar['close'][i]
    n_time = kbar['time'][i+1]
    n_open = kbar['open'][i+1]
    # 上一筆 MA
    last_s_ma=short_sma[i-1]
    last_l_ma=long_sma[i-1]
    # 當前 MA
    c_s_ma=short_sma[i]
    c_l_ma=long_sma[i]
    # 部位空手
    if index == 0:
        # ma 向上交叉的判斷
        if last_s_ma <= last_l_ma and c_s_ma > c_l_ma:
            index = 1
            order_time = n_time
            order_price = n_open
            stop_loss = order_price * (1-stop_ratio)
            continue
    elif index == 1:
        # 如果 收盤價乘上停損比率 大於 停損點
        if c_close * (1-stop_ratio) >= stop_loss:
            # 停損點上修
            stop_loss = c_close * (1-stop_ratio)
        if c_close <= stop_loss:
            index = 0 
            cover_time = n_time
            cover_price = n_open
            trade_record.append(['B',order_time,order_price,cover_time,cover_price])
            print('買進 時間: %s 價格: %s 出場 時間: %s 價格: %s' %(order_time,order_price,cover_time,cover_price) )
            


addp1.append(mpf.make_addplot(short_sma,color='#FFA488'))
addp1.append(mpf.make_addplot(long_sma,color='#CC0000'))
# 把 ma的畫圖物件 丟到 下單紀錄的圖表內 
chartOrder(kbar,trade_record,addp1)