from processing import *
from talib.abstract import *

#test______
stock_df =  get_stock_df('2303') 
stock_dict = transform_dict(stock_df)

short_sma=SMA(stock_dict,timeperiod=20)
long_sma=SMA(stock_dict,timeperiod=60)    


def buy():
    index = 1
    order_time = n_time #stock_dict['time'][i+1]
    order_price = n_open #stock_dict['open'][i+1]
    

def sell():
    index = 0 
    cover_time = n_time
    cover_price = n_open

def cross(short, long):
    if short < long & short.shift > long.shift:
        #golden_cross  buy
        pass
    elif short > long & short.shift < long.shift:
        #death cross   sell
        pass
    
    
#    RSI 50 ~ 80 , >80 , 20 ~ 50 , <20

trade_record=[]

index = 0

for i in range( 60+1 , len( stock_dict['time'] ) - 1):
    # 進出場時間
    #c_time = stock_dict['time'][i]
    #n_time = stock_dict['time'][i+1]
    n_open = stock_dict['open'][i+1]
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
            order_time = n_time #stock_dict['time'][i+1]
            order_price = n_open #stock_dict['open'][i+1]
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
performance(trade_record)

# # 把 ma的畫圖物件 丟到 下單紀錄的圖表內 
# chartOrder(stock_dict,trade_record,addp1)