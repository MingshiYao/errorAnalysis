# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:49:27 2020

@author: Hasee
"""

import math
import matplotlib.pyplot as plt
def sinee(x,n):
    term = x 
    sum = x

    for i in range(2,n):
      term = -term*x*x/((2*i - 1)*(2*i - 2)) 
      sum = sum + term 

    return sum
x = float(input("Enter an angle: "))
if x > 360: 
   x = x % 360
x=x/360*math.pi
logDiff=[0]*1000 # Array with 1000 elements 
logi=[0]*1000 # Array with 1000 elements 
for i in range(2,1002):
    
    if float(abs(sinee(x, i) - sinee(x, 2*i))) == 0:
        break
    
    logDiff[i-2] = math.log(abs(sinee(x, i) - sinee(x, 2*i)),10) 
    logi[i-2] = math.log(i-1,10)

plt.plot(logi,logDiff,"bo-")
plt.ylabel("logDiff")
plt.xlabel("logN")



