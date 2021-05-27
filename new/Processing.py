import pandas as pd 
#import numpy as np


def get_stock_df( stockno ):
    #for mpl use ,candlestick
    columns=['Time', 'Match_count', 'Match_value', 'Open', 'High', 'Low', 'Close', 'Diff', 'Volume']
    df = pd.read_csv(stockno +'.csv', parse_dates=[0], names = columns)
    #df['Symbol'] = stockno , 'Symbol'
    #TimeSeries index?
    #df = df.loc['2010-01-04':'2020-06-30',:]
    
    df[['Volume', 'Match_count', 'Match_value']] = df[['Volume', 'Match_count', 'Match_value']].astype('float64')
    df = df[['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Match_count', 'Match_value']]
    df.set_index( "Time" , inplace=True)
    #pd.set_option('display.max_columns', None)
    return df   
    
def transform_dict( df ):
    #for talib use, title lowercase
    stock_dict ={ 'time': df.index }
    for key in df.columns:
        stock_dict[key.lower()] = df[key].to_numpy()
    return stock_dict
        
#-----------------------------------------------------------------------------


    
def performance(trade_record):

    total_profit = []
    for i in trade_record:
        if i[0] == 'B':
            total_profit.append(i[4]-i[2])
        #elif i[0] == 'S':
        #    total_profit.append(i[2]-i[4])
            
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