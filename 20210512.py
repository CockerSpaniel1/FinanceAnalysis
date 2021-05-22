"""
開發日期:
開發人員:
最後修正日期:
修改人:
"""

import requests
from bs4 import BeautifulSoup

html=requests.get('https://tw.finance.yahoo.com/rank/turnover')
htmltext=html.text

soup=BeautifulSoup(htmltext)
ul=soup.find('ul' ,class_="M(0) P(0) List(n)")

f=open('C:\\Users\\16F-2\\Desktop\\pythonsample\\成交值排行.csv','a')

for li in ul.find_all('li'):
    tmplist=[]
    # 找到第一個超連結
    obj=li.find('a')
    # 依序去找到底下的div 總共11個
    for i in range(11):
        # 找到下一個div
        obj=obj.findNext('div')
        # 將逗點拿掉
        objtext=obj.text.replace(',','')
        # 如果資料是空值 則不加入list
        if objtext != '':
            tmplist.append(objtext)
    f.write(','.join(tmplist) + '\n')

f.close()
    

