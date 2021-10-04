#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
import random


# In[ ]:


while True:
    answer = int(input("graph equation or plot points? (1,2): "))
    if answer == 2:
        x = str
        y= str
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
        x = str
        y = str
        b = []
        xs = []
        r = []
        ys = []
        leftBound = int(input("Input LeftBound: "))
        rightBound = int(input("Input RightBound: "))
        equation = str(input("Equation: "))
        equation = equation.replace("y = ","")
        for i in range(rightBound):
            r = random.randint(leftBound, rightBound)
            xs.append(int(r))
            b.append(equation.replace("x", str(r)))
        print(xs)
        split = np.array_split(b,rightBound)
        for i in split:
            ys.append(eval(str(i))) 
            print(i)


# ## 

# In[ ]:




