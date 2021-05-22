from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
rsi=RSI(kbar,timeperiod=20)
short_sma=SMA(kbar,timeperiod=5)    # 前4筆是空值
long_sma=SMA(kbar,timeperiod=60)    # 前59筆是空值

import pandas as pd 
import numpy 
import mplfinance as mpf

Kbar_df=pd.DataFrame(kbar)
Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
Kbar_df.set_index( "Time" , inplace=True)

addp=[]
addp.append(mpf.make_addplot(short_sma))
addp.append(mpf.make_addplot(long_sma))
addp.append(mpf.make_addplot(rsi,panel='lower',secondary_y=False))
addp.append(mpf.make_addplot([30]* len(rsi),panel='lower',secondary_y=False,color='red'))
addp.append(mpf.make_addplot([70]* len(rsi),panel='lower',secondary_y=False,color='red'))

Kbar_df=Kbar_df

mpf.plot(Kbar_df,addplot=addp,volume=False,type='candle',style='charles')
 