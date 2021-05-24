# -*- coding: utf-8 -*-
"""
Created on Mon May 24 19:48:11 2021

@author: w
"""
import pandas as pd
df = pd.read_csv('semic.csv',encoding='big5')
print(df.head())
df.drop([0,1])
    