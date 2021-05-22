import datetime

data=open('i020.TXFA8').readlines()
data=[ i.strip('\n').split(',') for i in data ]

all_date= set([ i[0] for i in data ])
all_date= sorted(all_date)
# set 把所有重複資料唯一化

for date in all_date:
    # 單獨把每一天的資料都抓出來
    cdata=[ i for i in data if i[0]==date ]
    # 要把時間跟價格抓到
    Time= [ datetime.datetime.strptime(i[0]+i[1],'%Y%m%d%H%M%S%f') for i in cdata ]
    Price= [ float(i[3]) for i in cdata ]
    
    import matplotlib.pyplot as plt
    ax=plt.subplot(111)
    ax.plot_date(Time,Price,'k-')
    plt.show()
    
    break
    
    





