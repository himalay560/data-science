import statistics as p
import numpy as n
import math
import pandas as pa
data={'Name':n.array(['Tom','James','Ricky','Lee','David','Gasper','Betina','Andres']),
      'Age':n.array([25,26,25,23,30,29,23,34]),
      'Rating':n.array([1.00,2.020,3.221,4.543,5.436,6.00,7.123,8.901])}
#print(data)
s=pa.DataFrame(data)
print(s)
print(s.describe())
l=len(data['Age'])
l1=len(data['Rating'])
print(end="              ")
print("Age",end="    ")
print("Rating")
print("count",end="    ")
print(l,end="           ")
print(l1)
m=sum(data['Age'])/l
m1=sum(data['Rating'])/l1
print("mean",end="     ")
print(m,end="      ")
print(m1)
st=p.stdev(data['Age'])
st1=p.stdev(data['Rating'])
print("std",end="      ")
print('%.5f'%st,end="     ")
print('%.5f'%st1)
mi=min(data['Age'])
mi1=min(data['Rating'])
print("min",end="      ")
print(mi,end="          ")
print(mi1)
q1=n.percentile(data['Age'],25)
q11=n.percentile(data['Rating'],25)
print("25%",end="      ")
print(q1,end="        ")
print(q11)
q2=n.percentile(data['Age'],50)
q21=n.percentile(data['Rating'],50)
print("50%",end="      ")
print(q2,end="        ")
print(q21)
q3=n.percentile(data['Age'],75)
q31=n.percentile(data['Rating'],75)
print("75%",end="      ")
print(q3,end="       ")
print(q31)
ma=max(data['Age'])
ma1=max(data['Rating'])
print("max",end="      ")
print(ma,end="          ")
print(ma1)
