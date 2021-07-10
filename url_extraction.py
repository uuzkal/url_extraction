# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 00:07:41 2021

@author: Ugurhan Uzkal
"""

import pandas as pd

df = pd.read_csv('url_database.csv')

df_link = df['Stats_Access_Link']

for i in range(len(df_link)):
    df_link[i] = df_link[i].split('://')[1].split('</')[0]
    df.update(df_link)
    
df.to_csv('url_database_extracted.csv', index=False)