from haohaninfo import GOrder

GOC=GOrder.GOCommand()

def OrderMKT(broker,stock,bs,qty):
    OrderNo=GOC.Order(broker,stock,bs,"0",qty,"IOC","MKT","A")
    while True:
        OrderRS=GOC.GetAccount(broker, OrderNo)
        OrderInfo=OrderRS[0].split(',')
        print(OrderInfo)
        if OrderInfo[1] == '成交':
            return OrderInfo
            
# OrderMKT('Simulator_Stock','2615','B','1')
# OrderInfo=OrderMKT('Simulator_Stock','2014','B','1')
# print('成交時間 %s 成交價 %s'%(OrderInfo[7],OrderInfo[4]))

# ['S2021052600045,委託,3481,B,3.7,1000,ROD,2021/05/26 13:16:50,jacky55663399@gmail.com']
# ['S2021052600046,成交,3481,B,21.6,1000,IOC,2021/05/26 13:17:19,jacky55663399@gmail.com']

# 成交時間 44.05 成交價 2021/05/26 13:25:53
def GetPricebyTick(price,tick):
    StockPriceList=[]
    StockPriceList.extend([ i/100 for i in range(1,1001,1) ])
    StockPriceList.extend([ i/100 for i in range(1005,5005,5) ])
    StockPriceList.extend([ i/10 for i in range(501,1001,1) ])
    StockPriceList.extend([ i/10 for i in range(1005,5005,5) ])
    StockPriceList.extend([ i for i in range(501,1001,1) ])
    StockPriceList.extend([ i for i in range(1005,10005,5) ])
    return StockPriceList[StockPriceList.index(price)+tick]

# 限價單 到期刪單
import time
def OrderLMT(broker,stock,bs,price,qty,wait=10):
    OrderNo=GOC.Order(broker,stock,bs,price,qty,"ROD","LMT","A")
    EndTime=time.time()+wait
    while time.time() <= EndTime:
        OrderRS=GOC.GetAccount(broker, OrderNo)
        OrderInfo=OrderRS[0].split(',')
        if OrderInfo[1] == '成交':
            return OrderInfo
    GOC.Delete(broker, OrderNo)
    return False

# 範圍市價單 
def OrderRangeLMT(broker,stock,bs,price,qty,wait=10,tick=3):
    price=float(price)
    OrderPrice = GetPricebyTick(price,tick)
    OrderInfo=OrderLMT(broker,stock,bs,str(OrderPrice),qty,wait)
    return OrderInfo
        
# 範圍市價單直到成交(若買的話 我們不斷增加價格 來直到成交) 
# 取得價格
# 下單
# 判斷成交
# 刪單後 重新來過
def OrderRangeLMTtoDeal(broker,stock,bs,price,qty,wait=10):
    OrderPrice=float(price)
    while True:
        OrderPrice = GetPricebyTick(OrderPrice,1)
        OrderInfo=OrderLMT(broker,stock,bs,str(OrderPrice),qty,wait)
        if OrderInfo == False:
            continue
        elif OrderInfo[1] == '成交':
            return OrderInfo

