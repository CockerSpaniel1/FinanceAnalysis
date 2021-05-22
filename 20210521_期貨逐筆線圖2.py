import datetime

data=open('i020.TXFA8').readlines()
data=[ i.strip('\n').split(',') for i in data ]

all_date= set([ i[0] for i in data ])
all_date= sorted(all_date)
# set 把所有重複資料唯一化

for date in all_date:
    # 單獨把每一天的資料都抓出來
    cdata=[ i for i in data if i[0]==date ]
    print(cdata[0])
    # 要把時間跟價格抓到
    Time= [ datetime.datetime.strptime(i[0]+i[1],'%Y%m%d%H%M%S%f') for i in cdata ]
    Price= [ float(i[3]) for i in cdata ]
    
    
    # 平均買口數([6]/[7])-平均賣口數([6]/[8]) (口差)
    Sig1=[ float(i[6])/float(i[7])-float(i[6])/float(i[8]) for i in cdata ]
    
    import matplotlib.pyplot as plt
    ax1=plt.subplot(211)
    ax2=plt.subplot(212)
    ax1.plot_date(Time,Price,'k-')
    ax2.plot_date(Time,Sig1,'b-')
    ax2.plot_date(Time,[0]*len(Sig1),'k-')
    plt.show()
    
    break
    





