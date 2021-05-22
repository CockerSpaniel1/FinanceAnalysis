import datetime

data=open('i020.TXFA8').readlines()
data=[ i.strip('\n').split(',') for i in data ]

all_date= set([ i[0] for i in data ])
all_date= sorted(all_date)
# set 把所有重複資料唯一化

trade_record=[]
for date in all_date:
    # 單獨把每一天的資料都抓出來
    cdata=[ i for i in data if i[0]==date ]
    # 回測
    index = 0 
    for row in cdata:
        ctime=datetime.datetime.strptime(row[0]+row[1],'%Y%m%d%H%M%S%f')
        cprice=float(row[3])
        # 平均買口 平均賣口
        buy_count=float(row[6])/float(row[7])
        sell_count=float(row[6])/float(row[8])
        # 進場
        if index == 0 :
            if ctime.strftime('%H:%M')>='09:03':
                if buy_count > sell_count:
                    index = 1
                    order_time = ctime
                    order_price = cprice
                    continue
                else:
                    print(date,'當日不交易')
                    break
        elif index == 1 :
            if ctime.strftime('%H:%M')>='13:25':
                index = 0 
                cover_time = ctime
                cover_price = cprice
                trade_record.append(['B',order_time,order_price,cover_time,cover_price])
                print('多進場:%s 價位:%s 出場:%s 價位:%s' %(order_time,order_price,cover_time,cover_price))
                break

# 計算績效指標 
from myfunc import *
getPerformance(trade_record)




