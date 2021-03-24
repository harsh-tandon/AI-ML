#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:41:25 2021

@author: kumar
"""

import urllib
import pylab
import pandas as pd

pylab.rc('font', size=24)

URL = "https://api.bseindia.com/BseIndiaAPI/api/ProduceCSVForDate/w?strIndex=SENSEX&dtFromDate=01/01/2007&dtToDate=23/01/2021"

req = urllib.request.Request(URL,
    headers={
# Python/urllib ← Rejected by BSE website!
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })
u= urllib.request.urlopen(req)
df = pd.read_csv(u,
                 header=0, # ignore header
                 names = ['Date', 'Open',
                          'High', 'Low', 
                          'Close', 'Dummy'],
                          index_col = 'Date')

# How do we delete entries in a dictionary?
# del
del df['Dummy']
df.plot()
pylab.grid()

# 1. What is the intra-day swing limit for each day?
# i.e. what is the high - close for each day?
intraday_swings = (df['High'] - df['Low'])
intraday_swings.plot()
pylab.show()

# 2. How many times are there swings of more than
# 1000 points since the first date?
high_swings = df[intraday_swings.abs() >= 1000]
print(high_swings.count())

# 3. What is the fraction of positive
# days and negative days?
# i.e. Close - Open ≥ 0 and vice-versa?
daily_delta = (df['Close'] - df['Open'])
print("Market positive", 
      daily_delta[(daily_delta >= 0)].count() / daily_delta.count())
print("Market negative", 
      daily_delta[(daily_delta < 0)].count() / daily_delta.count())
print(daily_delta.describe())

# 4. On which day did we see the biggest fall?
print(daily_delta.idxmin())
daily_delta.hist(bins=50)


# 5. On which day did we see the biggest rise?
print(daily_delta.idxmax())

# 6. For better analysis:
day_delta = df['Close'][1:].to_numpy() - df['Close'][:-1].to_numpy()
df_delta = pd.DataFrame(data = day_delta, index=df.index[1:],
                        columns = ['delta'])
