'''
--------------------**** DATA ANALYSIS ****--------------------------
This is process of insepecting, cleaning, transfroming, and modeling, data
to discover useful insights

Types of DA
-----------
1.Descriptive Analysis
----------------------
-->Summarizing Causes

2.didnostic Anaysis
--------------------
-->Understanding Causes

3.Predictive Analysis
---------------------
-->Forecasting future outcomes

4.prescriptive Analysis
-----------------------
-->Suggesting actions based on data

Why Data Analysis
------------------
-->To improve Decision making
-->Dectects Trends & Patterns
-->

Numpy(Numerical Pyhton)
-----------------------
This python Library for numerical computing. It provides support for
multi-dimensional arrays, and linear algebra operations, making it essential
for data analysis...

Using numpy in Data Analysis
----------------------------
-->Improved performance
-->Simplifies complex operations
-->Easy data munipulation


import numpy as np
arr_1 = np.array([[1,2,3,4],[4,5,6,7],[1,2,3,8]])
print(arr_1)

import numpy as np
arr1 = np.array([[2,3,4],[4,5,6]])
print(arr1)
reshaped = arr1.reshape(6,1)
print(arr1.shape)
print(reshaped)

import numpy as np
arr1 = np.array([10,20,30,40,50,60,70])
print(arr1+30)

import numpy as np
arr1 = np.array([[3,4],[1,3]])
arr2 = np.array([[5,6],[7,8]])
print(np.dot(arr1,arr2))

import numpy as np
arr1 = np.array([10,20,30,40])
nrm_copy = arr1.view()
arr1[0] = 100
print(nrm_copy)
print(arr1)

copy_dee = arr1.copy()
arr1[1] = 400
print(copy_dee)
print(arr1)

Pandas
------
-->Is a powerful data manupulation and analysis library...
-->where it provides data structure like series and dataframe for efficient
data handling...

import pandas as pd
any_ = pd.Series([2999,15999,52999,6999,1999],index=['Earbuds','Smart phone','Laptop','Watch','Footware'])
print(any_)

method series
--------------
mean()
sum()
max()
min()
apply()
map()

Dataframe
----------


'''
import pandas as pd
data={
    'Product':['Earbuds','Smart phone','Laptop','Watch','Footware'],
    ' Brand' :['realme','iphone','macbook','HMT','nike'],
    'Price' :[3500,75000,150000,6400,4500],
    'quantity':[35,4,2,23,87]}
lip = pd.DataFrame(data)
print(lip)



























