from myfunc import *
# 取得資料 dictionary 格式 # 計算技術指標
kbar = getStockDaily_dict( '0050' )

from talib.abstract import *
short_rsi=RSI(kbar,timeperiod=20)
long_rsi=RSI(kbar,timeperiod=120)
# 計算 短線 減去 長線 的差異
rsi_diff=[ short_rsi[i]-long_rsi[i] for i in range(len(long_rsi)) ]

import pandas as pd 
import numpy 
import mplfinance as mpf

Kbar_df=pd.DataFrame(kbar)
Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
Kbar_df.set_index( "Time" , inplace=True)

addp=[]
# addp.append(mpf.make_addplot(short_rsi,panel='lower',secondary_y=False,color='#CA8EFF'))
# addp.append(mpf.make_addplot(long_rsi,panel='lower',secondary_y=False,color='#6F00D2'))
# addp.append(mpf.make_addplot([50]* len(long_rsi),panel='lower',secondary_y=False,color='red'))

addp.append(mpf.make_addplot(rsi_diff,panel='lower',secondary_y=False,color='#6F00D2'))
addp.append(mpf.make_addplot([0]* len(long_rsi),panel='lower',secondary_y=False,color='red'))

# [70,70,70,70,70]
# [30,40,50,60,70]
# [30,30,30,30,30]

Kbar_df=Kbar_df

mpf.plot(Kbar_df,addplot=addp,volume=False,type='candle',style='charles')
 