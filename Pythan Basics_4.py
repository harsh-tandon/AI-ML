# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:25:30 2021

Refer -> Global Module Index in python.org
data.splitlines()[1:]
%matplotlib inline
%matplotlib qt
urllib

Linear Regression Model
from sklearn import linear_model (Scikit)
"""

import urllib as ul
import pylab as pl

URL = "https://api.bseindia.com/BseIndiaAPI/api/ProduceCSVForDate/w?strIndex=SENSEX&dtFromDate=01/01/2018&dtToDate=23/01/2021"

req = ul.request.Request(URL, data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })

try:
    u = ul.request.urlopen(req)
except ul.request.HTTPError:
    print("Network Error. Sorry!")
        
data = u.read().decode('utf-8')
u.close()
print(data[0:990:])

sensex_date = []
sensex_close = []

for line in data.splitlines()[1:]:
    parts = line.split(',')
    sensex_date.append(parts[0])    
    sensex_close.append(float(parts[-2])) # default file text will be string

pl.plot(sensex_close)
pl.show()
 
print()
print('####################################################################')
print()

""" Linear Regression Model """

import urllib.request, pylab
import numpy as np
from sklearn import linear_model

URL = "https://api.bseindia.com/BseIndiaAPI/api/ProduceCSVForDate/w?strIndex=SENSEX&dtFromDate=01/01/2018&dtToDate=23/01/2021"

req = urllib.request.Request(URL,
                            data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })

u = urllib.request.urlopen(req)
data = str(u.read()).replace("\\r\\n", "\n")
u.close()
dates = []
sensex = []

for line in data.splitlines()[1:]:
    line = line[:-2]
    line = line.split(',')
    if len(line) > 1:
        dates.append(line[0])
        sensex.append(float(line[-1]))

sensex = np.array(sensex)
days = np.arange(len(sensex))
regr = linear_model.LinearRegression()

M = 30 # last how many days' data do we use for prediction?
regr.fit(days[-M:].reshape(-1, 1), sensex[-M:].reshape(-1,1))
future_days = days[-1] + np.arange(30)
pred = regr.predict(future_days.reshape(-1,1))
pylab.plot(days, sensex)
pylab.plot(future_days, pred)
pylab.show()

    
 

