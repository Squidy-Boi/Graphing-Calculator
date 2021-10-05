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
from sympy import *
import random


# In[ ]:


def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)
    plt.show()

def graph2(formula, x_range, color, lowerBound, upperBound):
    x = np.array(x_range)
    y = eval(formula)
    plt.ylim(lowerBound,upperBound)
    plt.plot(x,y)
    
while True:
    while True:
        try:
            answer = int(input("graph equation, plot points, solve an equation, or graph multiple? (1,2,3,4): "))
            if answer == 1:
                break
            elif answer == 2:
                break
            elif answer == 3:
                break
            elif answer == 4:
                break
        except ValueError:
            answer = 0
            print("invalid syntax: 1,2,3 or 4")
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
    elif answer == 1: 
        leftBound = int(input("Enter LeftBound: "))
        rightBound = int(input("Enter RightBound: "))
        userEq = input("Enter Equation: y = ")
        
        graph(userEq, range(leftBound, rightBound))
    elif answer == 3:
        while True:  
            userEq = input("Enter Equation y = ")
            xval = input("Enter x value: ")
            userEq = userEq.replace("x", xval)
            try: 
                y = eval(userEq)
                print("The answer is: " + str(y))
                break
            except ZeroDivisionError:
                print("Undefined")
                break
            except SyntaxError:
                print("invalid syntax retype expression")
                y 
            except NameError:
                print("invalid syntax retype expression")
    elif answer == 4:
        color = ["r","b","g","c","m","y","w","k"]
        amt = 0
        
        amt = int(input("How many graphs? (max of 8): "))
        if amt > 8:
            while amt > 8:
                amt = int(input("How many graphs? (max of 8): "))
        leftBound = int(input("Enter LeftBound: "))
        rightBound = int(input("Enter RightBound: "))
        upperBound = int(input("Enter UpperBound: "))
        lowerBound = int(input("Enter LowerBound: "))
        for i in range(amt):
            tempColor = color[0]
            userEq = input("Enter Equation: y =")
            graph2(userEq, range(leftBound,rightBound),tempColor,lowerBound,upperBound)
            color.pop(0)
        plt.show()


# In[ ]:





# In[ ]:




