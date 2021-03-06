from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
short_sma=SMA(kbar,timeperiod=5)
long_sma=SMA(kbar,timeperiod=60)

import pandas as pd 
import numpy 
import mplfinance as mpf

Kbar_df=pd.DataFrame(kbar)
Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
Kbar_df.set_index( "Time" , inplace=True)

addp=[]
addp.append(mpf.make_addplot(short_sma,color='#FFA48B'))
addp.append(mpf.make_addplot(long_sma,color='#CC0000'))

mpf.plot(Kbar_df,addplot=addp,volume=True,type='candle',style='charles')
 