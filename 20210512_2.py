import requests,json,time

def ConverYear(a):
    b=a.split('/')
    b1=int(b[0])+1911
    b1=str(b1)
    return '/'.join([b1,b[1],b[2]])

response='json'
stockNo='2014'
timestamp='1620788646060'

total_data = []
for date in ['20210101','20210201','20210301','20210401','20210501']:
    
    # date='20210401'

    html=requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response='+response+'&date='+date+'&stockNo='+stockNo+'&_='+timestamp)

    data=json.loads(html.text)

    for row in data['data']:
        row[0]=ConverYear(row[0])
        row=[ i.replace(',','') for i in row ]
        print(row)
        total_data.append(row)
        
    time.sleep(5)

f=open('C:\\Users\\16F-2\\Desktop\\pythonsample\\'+stockNo+'.csv','a')

for row in total_data:
    f.write(','.join(row) + '\n')

f.close()