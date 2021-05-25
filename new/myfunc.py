import datetime #pymysql
import pandas as pd 
import numpy as np
import mplfinance as mpf

def getStockDaily( stockno ):
    columns=['Time', 'Match_count', 'Match_value', 'Open', 'High', 'Low', 'Close', 'Diff', 'Volume']
    df = pd.read_csv(stockno+'.csv',names = columns)
    df['Symbol'] = stockno
    df['Time'] = pd.to_datetime(df['Time'])
    df[['Volume', 'Match_count', 'Match_value']] = df[['Volume', 'Match_count', 'Match_value']].astype('float64')
    df = df[['Time', 'Symbol', 'Open', 'High', 'Low', 'Close', 'Diff', 'Volume', 'Match_count', 'Match_value']]
    
    return df
    #pd.set_option('display.max_columns', None)
    
    
    
def getStockDaily_dict( stockno ):
    data=getStockDaily( stockno )
    data_dict ={}
    for key in data.columns:
        data_dict[key] =data[key].to_numpy()
    return data_dict
        
        
#--current       
    
#def getStockDaily_df(stockno):
    #kbar=getStockDaily_dict( stockno )
    #Kbar_df=pd.DataFrame(kbar)
    #Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
    #Kbar_df.set_index( "Time" , inplace=True)
    #return Kbar_df
#-----------------------------------------------------------------------------
    
def chartKbar(df):
    Kbar_df=df.set_index( "Time" , inplace=True)
    mpf.plot(Kbar_df,volume=True,type='candle',style='charles')
    
def chartKbar_dict(Kbar):
    Kbar_df=pd.DataFrame(Kbar)
    #Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
    Kbar_df.set_index( "Time" , inplace=True)
    mpf.plot(Kbar_df,volume=True,type='candle',style='charles')
    
def chartOrder(Kbar,TR,addp=[]):
    Kbar_df=pd.DataFrame(Kbar)
    #Kbar_df.columns = [ i[0].upper()+i[1:] for i in Kbar_df.columns ]
    Kbar_df.set_index( "Time" , inplace=True)
    
    # add plot   
    BTR = [ i for i in TR if i[0]=='B' ]
    # 如果我有買方 交易紀錄的話 圖表才顯示買方交易
    if BTR != []:
        BuyOrderPoint = [] 
        BuyCoverPoint = []
        for date,value in Kbar_df['Close'].iteritems():
            # 日期 在 買方 進場 交易記錄內 
            if date in [ i[1] for i in BTR ]:
                # 新增一個值 最低點的 下面
                BuyOrderPoint.append( Kbar_df['Low'][date] * 0.999 )
            else:
                # nan
                BuyOrderPoint.append(np.nan)
            if date in [ i[3] for i in BTR ]:
                BuyCoverPoint.append( Kbar_df['High'][date] * 1.001 )
            else:
                BuyCoverPoint.append(np.nan)
        addp.append(mpf.make_addplot(BuyOrderPoint,scatter=True,markersize=20,marker='^',color='red'))
        addp.append(mpf.make_addplot(BuyCoverPoint,scatter=True,markersize=20,marker='v',color='blue'))
    STR = [ i for i in TR if i[0]=='S' ]
    if STR != []:
        SellOrderPoint = [] 
        SellCoverPoint = []
        for date,value in Kbar_df['Close'].iteritems():
            # 日期 在 賣方 進場 交易記錄內 
            if date in [ i[1] for i in STR ]:
                # 新增一個值 最高點的 上面
                SellOrderPoint.append( Kbar_df['High'][date] * 1.001 )
            else:
                # nan
                SellOrderPoint.append(np.nan)
            if date in [ i[3] for i in STR ]:
                SellCoverPoint.append( Kbar_df['Low'][date] * 0.999 )
            else:
                SellCoverPoint.append(np.nan)
        addp.append(mpf.make_addplot(SellOrderPoint,scatter=True,markersize=200,marker='v',color='green'))
        addp.append(mpf.make_addplot(SellCoverPoint,scatter=True,markersize=200,marker='^',color='blue'))
    
    mpf.plot(Kbar_df,addplot=addp,volume=False,type='candle',style='charles')
    
def getPerformance(TR):

    total_profit = []
    for i in TR:
        if i[0] == 'B':
            total_profit.append(i[4]-i[2])
        elif i[0] == 'S':
            total_profit.append(i[2]-i[4])
            
    earn_total_profit=[ i for i in total_profit if i > 0 ]
    loss_total_profit=[ i for i in total_profit if i <= 0 ]

    # 最大連續虧損
    max_loss=0
    current_max_loss=0
    for i in total_profit:
        if i <= 0:
            current_max_loss += i
            if current_max_loss < max_loss:
                max_loss = current_max_loss
        else:
            current_max_loss = 0 
            
    print('\n總績效',sum(total_profit),'總次數',len(total_profit))
    print('平均績效',sum(total_profit)/len(total_profit))
    print('平均獲利',sum(earn_total_profit)/len(earn_total_profit))
    print('平均損失',sum(loss_total_profit)/len(loss_total_profit))
    print('勝率',len(earn_total_profit) / len(total_profit))
    print('最大連續虧損',max_loss)
    print('獲利因子',sum(earn_total_profit)/abs(sum(loss_total_profit)))
#-----------------------------------------------------------------------------