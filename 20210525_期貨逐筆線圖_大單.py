import datetime
import matplotlib.pyplot as plt

data=open('i020.TXFA8').readlines()
data=[ i.strip('\n').split(',') for i in data ]

all_date= set([ i[0] for i in data ])
all_date= sorted(all_date)
# set 把所有重複資料唯一化

for date in all_date:
    # 單獨把每一天的資料都抓出來
    cdata=[ i for i in data if i[0]==date ]
    
    big_b_time=[]
    big_b_price=[]
    big_s_time=[]
    big_s_price=[]
    big_b_amount=0
    big_s_amount=0
    big_b_amount_list=[]
    big_s_amount_list=[]
    for i in range(1,len(cdata)):
        c_time=ctime=datetime.datetime.strptime(cdata[i][0]+cdata[i][1],'%Y%m%d%H%M%S%f')
        c_price=float(cdata[i][3])
        # 取得當前資料
        c_amount=int(cdata[i][6])
        c_b_count=int(cdata[i][7])
        c_s_count=int(cdata[i][8])
        # 取得上一筆資料
        last_amount=int(cdata[i-1][6])
        last_b_count=int(cdata[i-1][7])
        last_s_count=int(cdata[i-1][8])
        # 計算變動量
        diff_amount=c_amount-last_amount
        diff_b_count=c_b_count-last_b_count
        diff_s_count=c_s_count-last_s_count
        # 數量大於 n 口 把它定義為大量
        if diff_amount > 20:
            # 一個人買 多個人賣
            if diff_b_count == 1 and diff_s_count > 1:
                # 買方進單
                print(c_time,'價格',c_price,'B 大單量',diff_amount,' S',diff_s_count,'人')
                big_b_amount += diff_amount
                big_b_time.append(c_time)
                big_b_price.append(c_price)
                big_b_amount_list.append(big_b_amount)
            elif diff_s_count == 1 and diff_b_count > 1:
                # 賣方進單
                print(c_time,'價格',c_price,'S 大單量',diff_amount,' B',diff_b_count,'人')
                big_s_amount += diff_amount
                big_s_time.append(c_time)
                big_s_price.append(c_price)
                big_s_amount_list.append(big_s_amount)
    
    Time= [ datetime.datetime.strptime(i[0]+i[1],'%Y%m%d%H%M%S%f') for i in cdata ]
    Price= [ float(i[3]) for i in cdata ]
    Sig1=[ float(i[6])/float(i[7])-float(i[6])/float(i[8]) for i in cdata ]
    ax1=plt.subplot(211)
    ax2=plt.subplot(212)
    ax1.plot_date(Time,Price,'k-')
    ax1.plot_date(big_b_time,big_b_price,'ro')
    ax1.plot_date(big_s_time,big_s_price,'go')
    # ax2.plot_date(Time,Sig1,'b-')
    # ax2.plot_date(Time,[0]*len(Sig1),'k-')
    ax2.plot_date(big_b_time,big_b_amount_list,'r-')
    ax2.plot_date(big_s_time,big_s_amount_list,'g-')
    plt.show()
    
    # break
    





