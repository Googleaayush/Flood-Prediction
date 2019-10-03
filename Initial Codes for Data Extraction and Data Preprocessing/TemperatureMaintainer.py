# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:23:33 2019

@author: Ayush Jain
"""

import pandas as pd
import os

m=os.listdir()
print(m[0].split(".")[0])


from itertools import cycle
for t in range(0,len(os.listdir())-2):

 data=pd.read_csv(m[t ],usecols=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
       'Oct', 'Nov', 'Dec'])
 data=data.T
 data=pd.Series(data.values.ravel('F'))
 data1=pd.DataFrame(data.values, columns = ["AvgTemp" ])

 repeat_arr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
       'Oct', 'Nov', 'Dec']
#data = data.join(pd.DataFrame(repeat_arr * (len(data)/len(repeat_arr)+1),
#    columns=['month']))
 seq = cycle(repeat_arr)
 data1['mon'] = [next(seq) for count in range(data.shape[0])]
 list1=[];
 list2=[]; 
 for i in range(1952,2003):
    for j in range(0,12):
        list1.append(i)
        list2.append(m[t].split(".")[0])
 data1['year']=list1
 data1['DISTRICT']     
 data1.to_csv(m[t].split(".")[0]+".csv",index=False)
