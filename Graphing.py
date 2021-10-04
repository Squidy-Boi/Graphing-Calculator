#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install plotly')
get_ipython().system(' pip install cufflinks')
get_ipython().system(' pip install chart_studio')
get_ipython().system(' pip install matplotlib')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cufflinks as cf
import plotly.offline as py
import plotly.tools as tls
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px
import math
from sympy import *
import random


# In[17]:


while True:
    answer = int(input("graph equation or plot points? (1,2): "))
    if answer == 2:
        x = str
        y = str
        b = []
        d = []
        leftBound = int(input('Input Leftbound: '))
        rightBound = int(input('Input Rightbound: '))
        amt = int(input('amount of data: '))
        a = np.linspace(start=leftBound,stop=rightBound,num=amt)
        for i in range(amt):
            b.append(int(input("Enter X: ")))
            d.append(int(input("Enter Y: ")))
        fig = px.scatter(x=b,y=d,trendline='ols')
        fig.show()
        break
    elif answer == 1:
        x, y = symbols('x y')
        b = []
        xs = []
        r = []
        ys = []
        nums = int(input("Input amount of Data: "))
        equation = str(input("Equation: y = "))
        for i in range(nums):
            r = int(i)
            xs.append(int(r))
            b.append(equation.replace("x", str(r)))
            tempeq = equation.replace("x",str(i))
            try:
                temp = eval(tempeq)
            except ZeroDivisionError:
                print("0 lmao")
            print(temp)
            ys.append(temp)
        fig = px.scatter(x=xs,y=ys)
        fig.show()
        break


# ### 

# In[ ]:




