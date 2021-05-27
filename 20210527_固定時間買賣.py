from haohaninfo import GOrder
import datetime
from order_bigdata import OrderMKT

BK='Simulator_Stock'
STK='3481'

T1='1023'
T2='1022'

GOQ=GOrder.GOQuote()
Index = 0 
for row in GOQ.Subscribe( BK , 'match', STK ):
    # ['2021/05/27 10:08:24.656481', '2615', '140.5', '10', '88258', '140', '140.5']
    print(row)
    T=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    T0=T.strftime('%H%M')
    
    if Index == 0:
        print(T0,T1)
        if T0 >= T1 :
            Index = 1
            OINFO=OrderMKT(BK,STK,'B','1')
            print('進場成功',OINFO)
            break
            
