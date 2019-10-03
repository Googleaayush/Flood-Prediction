# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 00:49:56 2019

@author: Ayush Jain
"""

import pandas as pd
import os

m=os.listdir()
print(m[0].split(".")[0])

for i in range(0,len(os.listdir())-1):
    
    data = pd.read_csv(m[i],delimiter="\t")
    df=pd.DataFrame(data)
    df.to_csv(m[i].split(".")[0]+".csv",index=False,float_format='%.3f')
