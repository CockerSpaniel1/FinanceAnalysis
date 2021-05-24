import datetime

# 定義起始 結束日
begin=datetime.datetime.strptime('2010/01/01','%Y/%m/%d')
end=datetime.datetime.strptime('2021/05/01','%Y/%m/%d')

date_list=[]
while begin<=end:
    # 顯示日期
    date_str=begin.strftime('%Y%m%d')
    date_list.append(date_str)
    # 往下一個月
    begin += datetime.timedelta(days=31)
    begin=begin.replace(day=1)

print(date_list)

# 分隔線-----------------------------------

import requests,json,time

def ConverYear(a):
    b=a.split('/')
    b1=int(b[0])+1911
    b1=str(b1)
    return '/'.join([b1,b[1],b[2]])

response='json'
stockNo='2002'
timestamp='1621490872557'

total_data = []
for date in date_list:
    try:
        html=requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response='+response+'&date='+date+'&stockNo='+stockNo+'&_='+timestamp)
        data=json.loads(html.text)
        for row in data['data']:
            row[0]=ConverYear(row[0])
            row=[ i.replace(',','') for i in row ]
            # print(row)
            total_data.append(row)
        print(date,'爬蟲成功')
        time.sleep(5)
    except:
        print(date,'爬蟲失敗')
        break

# 分隔線-----------------------------------

#f=open('C:\\Users\\16F-2\\Desktop\\pythonsample\\'+stockNo+'.csv','a')
f=open(stockNo+'.csv','a')

for row in total_data:
    f.write(','.join(row) + '\n')

f.close()

# 分隔線-----------------------------------
f=open(stockNo+'.csv')
data = [ i.strip('\n').split(',') for i in f ]

# 分隔線-----------------------------------
"""
import pymysql
# localhost = 127.0.0.1
conn=pymysql.connect(host='localhost', port=3306, user="root",passwd="123456",db="fintech")
# 建立工作環境(游標)
cur = conn.cursor() 

for row in data:
    execstr="insert into stock_daily value ('%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (stockNo,row[0],row[3],row[4],row[5],row[6],row[1],row[8],row[2])
    cur.execute( execstr )

conn.commit()
cur.close()
conn.close()
"""
