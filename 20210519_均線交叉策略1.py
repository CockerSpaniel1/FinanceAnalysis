from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
short_sma=SMA(kbar,timeperiod=5)    # 前4筆是空值
long_sma=SMA(kbar,timeperiod=60)    # 前59筆是空值

# 交易紀錄的物件
trade_record=[]

index = 0
for i in range(60+1,len(kbar['time'])-1):
    # 進出場時間
    c_time = kbar['time'][i]
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
            continue
    elif index == 1:
        # MA 快線 向下穿越 慢線 多單出場
        if last_s_ma >= last_l_ma and c_s_ma < c_l_ma:
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
addp1.append(mpf.make_addplot(short_sma,color='#FFA488'))
addp1.append(mpf.make_addplot(long_sma,color='#CC0000'))
# 把 ma的畫圖物件 丟到 下單紀錄的圖表內 
chartOrder(kbar,trade_record,addp1)