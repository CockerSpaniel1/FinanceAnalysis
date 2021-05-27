# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:36:55 2021

@author: w
"""
#df for mpl
from processing import *
#dict for talib


stock_df =  get_stock_df('2303') 
stock_dict = transform_dict(stock_df)

# import drawing

# t=drawing.addp
# print(t)