# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:48:11 2021

@author: w
"""
import pandas as pd
df = pd.read_csv('semic.csv',encoding='big5')
#print(df.head())
#df.iloc[0:2,0]

#df = df.iloc[3:]
#print(df)
df.drop(df.head(2).index, inplace=True)
df.drop(df.tail(5).index, inplace=True)

#print(df.index)
semicID = list(df.index.get_level_values(0))

semic_dict = dict(zip(df.index.get_level_values(0),df.index.get_level_values(1)))

from new.StockCrawler import *

for stockid in semicID:
    crawl_stock(stockid)
