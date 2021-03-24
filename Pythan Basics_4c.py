# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 21:58:32 2021

%matplotlib inline
%matplotlib qt

pandas (Series, Dataframe) 
numpy (array)
These are interchangeable
np.random.randn(1000) - get list with 1000 random (small -ve and +ve) values
pd.date_range(start='20200101', end='20201231')
set(multiples_of_3).union(set(multiples_of_5)) # convert list to set to use union()
df = pd.DataFrame(np.random.randn(6, 4))  6x4 matrix of small -ve/+ve values
df.loc['20210228':'20210531',['A','B']]  Multiple slicing
df.iloc[3:5, 0:3]  # Row, Col slicing

"""

import numpy as np
import pandas as pd

a1 = np.array([1, 2.3, "test"])
print(a1)
print(type(a1[1])) # all elements are stored as string

a1 = np.array([1, 2.3, 3.2])  # all elements are stored as float
print('a1', a1)
s1 = pd.Series(a1)
print('s1', s1)
print(s1.to_numpy())
print()

#assert((a1 == s1.to_numpy()).all())
df = pd.read_csv('marks2.csv', index_col='Rollnumber')

# Find the maximum score in Chemistry
print('Max chemistry score', df['Chemistry'].max())
print('Max physics scorer', df['Physics'].idxmax())
print()

print(df.loc[df['Maths'].idxmax()])
print(df.loc[df['Maths'].idxmax()]['Name'])
print()

print(df.loc['R1'])
print(df.dtypes)
print()

print(df.sort_values(by='Chemistry', ascending=True))
print()

print((df['Maths'] + df['Physics'] + df['Chemistry']).sort_values())
print((df['Maths'] + df['Physics'] + df['Chemistry']).to_list())
print()

# Let us add the Biology score
df2 = df.assign(Biology = [60, 70, 55, 62])
print(df2)
print(df2['Biology'].to_numpy())

print('################### 1 #################################################')

# Appending data frames
df1 = pd.read_csv('marks2.csv', index_col='Rollnumber')
df2 = pd.read_csv('marks3.csv', index_col='Rollnumber')
df_total = df1.append(df2)
print("df_total\n", df_total)
print()

df3 = pd.read_csv('marks2_extra.csv', index_col = 'Rollnumber')
df_combined = pd.merge(df1, df3)
print("df_combined\n", df_combined)
print()

# 1. Let us read the poorly made file
df = pd.read_csv('badmarks.csv', index_col='Name').fillna(0)
print("Bad marks:\n", df)

print()
print('#################### 2 ################################################')
print()

temperatures = np.random.randn(1000) * 4 + 25  # 1000 random values
print(temperatures)
df = pd.DataFrame(data=temperatures, columns=['Temperature'])
df['Temperature'].hist(bins=100)

print()
print('##################### 3 ###############################################')
print()

# Date series with Dataframe
days_in_2020 = pd.date_range(start='20200101', end='20201231')
print(days_in_2020)
print()

months = pd.date_range(start='20200101', end='20201231', freq='M')
print(months)
print()

time_range = pd.date_range(start='20200101', end='20201231', freq='s')[:-1]  # drop midnight of next day
print(time_range)
print(len(time_range))

temp_data = 24 + 5 * np.random.randn(len(time_range))
df = pd.DataFrame(data=temp_data, columns=['Temperature'], index=time_range)

temp_data = 24 + 5 * np.random.randn(len(months))
temp_data_2 = 28 + 5 * np.random.randn(len(months))

df = pd.DataFrame(data=np.array([temp_data, temp_data_2]).T, 
                  columns=['Delhi', 'Mumbai'], index=months)
df.plot()

data=np.array([temp_data, temp_data_2]).T
print(data)

print()
print('##################### 4 ###############################################')
print()

data = """A,B,C
1,2,3
4,5,6"""

from io import StringIO
data = pd.read_csv(StringIO(data))
print(data)

print()
print('###################### 5 ##############################################')
print()

# Find all numbers which are multiple of 3 or 5.
def multiple_3_5(N1, N2):
    all_numbers = list(range(N1, N2+1))
    multiples_of_3 = [i for i in all_numbers if i % 3 ==0]
    multiples_of_5 = [i for i in all_numbers if i % 5 ==0]
    mul_3_5 = set(multiples_of_3).union(set(multiples_of_5)) # convert list to set to use union()
    print(set(multiples_of_3))
    print(mul_3_5)
    return len(mul_3_5)

print(multiple_3_5(1, 10))
print()
print(multiple_3_5(1, 100))
print()

x = [1, 2, 3, 10, 9]
print(x[::-1])  # Reverse anything [::-1]
print(("Kumar"[::-1]))  # Reverse anything [::-1]

print()
print('################## SERIES #####################')
print()

srdates = pd.date_range('20210215', periods=6, freq='M')  # yyyyMMdd, period = 6 = rows
print(srdates)
print()

df = pd.DataFrame(np.random.randn(6, 4), columns = list('ABCD'), index=srdates) # 6x4 matrix of small -ve/+ve values, list('ABCD') = 4 cols
print(df) 
print(df.columns)  # Column header name
print()

print(df.values)  # Column header name
print(sum(df.values[0]))
print()

print((df.values.T)[1:3].T)  # Slicing with Matrix Transpose
print()

print(df.describe()) # Get mean, std, max
print()

print(df.head(3)) # Top 3
print(df.tail(2)) # Bottom 2
print()

print()
print('###################### 6 ##############################################')
print()

print("Index sorting\n", df.sort_index(ascending=False, axis=1)) # reverse cols
print()

print("Sort by Col B\n", df.sort_values(by='B'))
print()

print("Only Col B\n", df['B'])
print()

print('Only A, B Cols\n', df.loc[:,['A', 'B']]) # Slice only A & B columns
print()

# Value wise filter
print(df.loc['20210228':'20210531',['A','B']])  # Multiple Slicing
print(df.loc['20210228', ['A','B']])  # Multiple Slicing
print(df.loc['20210228', ['A']])  # Multiple Slicing
print()

print()
print('###################### 7 ##############################################')
print()

# Index wise filter
print(df.iloc[3:5, 0:3])  # Row, Col slicing
print(df.iloc[:, 0:3])  # Only Col slicing
print(df[df.A > 0])  # conditional filter
print()

df = df[df > 0]  # replace -ve values with NaN
print(df.fillna(value=0.5555))
print()

print(df.mean())  # mean(1) for other axis




















