data=open('i020.TXFA8').readlines()
data=[ i.strip('\n').split(',') for i in data ]

all_date= set([ i[0] for i in data ])
all_date= sorted(all_date)
# set 把所有重複資料唯一化

for date in all_date:
    # 單獨把每一天的資料都抓出來
    print(date)
    cdata=[ i for i in data if i[0]==date ]
    print(cdata[0])
    print(cdata[-1])
    





