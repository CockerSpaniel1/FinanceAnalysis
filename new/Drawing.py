import mplfinance as mpf
from talib.abstract import *

addp=[]
#iday = intraday.loc['2019-11-05':'2019-11-06',:]
def draw_candlestick(df):
    df.set_index( "Time" , inplace=True)
    mc = mpf.make_marketcolors(up='red', down='black')
    s = mpf.make_mpf_style(base_mpf_style = 'charles',marketcolors=mc)
    mpf.plot(df,addplot=addp, volume=True, type='candle', style=s)


def append_MA(dic):
    month_MA= SMA(dic,timeperiod=20)
    quarter_MA = SMA(dic,timeperiod=60)  

    addp.append(mpf.make_addplot(month_MA) ) #,color='#FFA488'))
    addp.append(mpf.make_addplot(quarter_MA) ) #,color='#CC0000')) 


def append_RSI(dic):
    rsi=RSI(stock_dict , timeperiod=20)
    addp.append(mpf.make_addplot(rsi,panel='lower',secondary_y=False))
    addp.append(mpf.make_addplot([50]* len(rsi),panel='lower',secondary_y=False,color='red'))
    #addp.append(mpf.make_addplot([70]* len(rsi),panel='lower',secondary_y=False,color='red'))
    #(30,70)
    
#-----
from myfunc import get_stock_df, transform_dict
stock_df =  get_stock_df('0050') 
stock_dict = transform_dict(stock_df)
draw_candlestick(stock_df)
#-------
#____________________________________________
# def chartOrder(df, record, addp=[]):
#     df.set_index( "Time" , inplace=True)
    
    
#     BTR = [ i for i in record if i[0]=='B' ]

#     if BTR != []:
        
#         BuyOrderPoint = [] 
#         BuyCoverPoint = []
        
        
#         for date,value in df['Close'].iteritems():

#             if date in [ i[1] for i in BTR ]:
#                 BuyOrderPoint.append( df['Low'][date] * 0.999 )
#             else:
#                 BuyOrderPoint.append(np.nan)
#             if date in [ i[3] for i in BTR ]:
#                 BuyCoverPoint.append( df['High'][date] * 1.001 )
#             else:
#                 BuyCoverPoint.append(np.nan)
                
#         addp.append(mpf.make_addplot(BuyOrderPoint,scatter=True,markersize=20,marker='^',color='red'))
#         addp.append(mpf.make_addplot(BuyCoverPoint,scatter=True,markersize=20,marker='v',color='blue'))
#____________________________________________

# #Rsi and ma
# rsi=RSI(kbar,timeperiod=20)
# short_sma=SMA(kbar,timeperiod=5)    # 前4筆是空值
# long_sma=SMA(kbar,timeperiod=60)    # 前59筆是空值


# addp=[]
# addp.append(mpf.make_addplot(short_sma))
# addp.append(mpf.make_addplot(long_sma))
# addp.append(mpf.make_addplot(rsi,panel='lower',secondary_y=False))
# addp.append(mpf.make_addplot([30]* len(rsi), panel='lower',secondary_y=False,color='red'))
# addp.append(mpf.make_addplot([70]* len(rsi),panel='lower',secondary_y=False,color='red'))


#_________________________________________________________
  

# short_rsi=RSI(kbar,timeperiod=20)
# long_rsi=RSI(kbar,timeperiod=120)
# # 計算 短線 減去 長線 的差異
# rsi_diff=[ short_rsi[i]-long_rsi[i] for i in range(len(long_rsi)) ]

# addp=[]
# # addp.append(mpf.make_addplot(short_rsi,panel='lower',secondary_y=False,color='#CA8EFF'))
# # addp.append(mpf.make_addplot(long_rsi,panel='lower',secondary_y=False,color='#6F00D2'))
# # addp.append(mpf.make_addplot([50]* len(long_rsi),panel='lower',secondary_y=False,color='red'))

# addp.append(mpf.make_addplot(rsi_diff,panel='lower',secondary_y=False,color='#6F00D2'))
# addp.append(mpf.make_addplot([0]* len(long_rsi),panel='lower',secondary_y=False,color='red'))

# mpf.plot(Kbar_df,addplot=addp,volume=False,type='candle',style='charles')
#__________________________________________________________
from talib.abstract import *
upper,middle,lower=BBANDS(kbar,timeperiod=20)

import pandas as pd 
import numpy 
import mplfinance as mpf

addp=[]
addp.append(mpf.make_addplot(upper))
addp.append(mpf.make_addplot(middle))
addp.append(mpf.make_addplot(lower))
# addp.append(mpf.make_addplot(rsi,panel='lower',secondary_y=False))
# addp.append(mpf.make_addplot([30]* len(rsi),panel='lower',secondary_y=False,color='red'))
# addp.append(mpf.make_addplot([70]* len(rsi),panel='lower',secondary_y=False,color='red'))

Kbar_df=Kbar_df

mpf.plot(Kbar_df,addplot=addp,volume=False,type='candle',style='charles')
 
 