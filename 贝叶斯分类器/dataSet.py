# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:34:09 2020

@author: zhao
"""
import json

b=''
with open('a.json',encoding='utf-8') as f:
    a=''
    a=f.read()
    a='['+a.replace("}{","},{").replace('\n','').replace('\r','').replace('\r\n','').replace(' ','')+']';
    b=json.loads(a)
    #print(b)
    f.close()
data=[]
for i in range(len(b)):
    dataSet=b[i].values()
    dataSet=list(dataSet)
    h1=dataSet[2]
    h2=dataSet[-1]
    h3=[h1,h2]
    data.append(h3)
    
for i in range(len(data)):
    print(data[i][1])

data[0][1]='建筑业'
   