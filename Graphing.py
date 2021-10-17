# fucking I M P O R T
import matplotlib.pyplot as plt
import numpy as np # <--- literally the best fucking thing you could ever import to python
import pandas as pd
import cufflinks as cf
import plotly.express as px
import math
from sympy import *
import random
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# use for one graph
def graph(formula, x_range):  
    plt.figure().clear() 
    x = np.array(x_range)  
    y = eval(formula) #notice how I dont check for ZeroDivisionError but still functions, the beauty of matplotlib autochecking errors
    plt.plot(x, y)
    plt.show()

# use for multigraph
def graph2(formula, x_range, color, lowerBound, upperBound): 
    x = np.array(x_range)
    y = eval(formula)
    plt.ylim(lowerBound,upperBound)
    plt.plot(x,y,color=color)

# use for surface graph
def surface(x,y):
  plt.figure().clear() 
  x,y = np.meshgrid(x,y)
  r = np.sqrt(x**2 + y**2)
  z = np.sin(r)
  fig = plt.figure()
  axes = Axes3D(fig, auto_add_to_figure=false)
  fig.add_axes(axes)
  axes.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.viridis)

# main graphing function that allows the user to choose between 5 modes, Graphing an equation, plotting points, simple equation solver (one x variable), graph multiple equations on one graph, or graph a surface plot.
def graphing():
    while True: # main loop 
      plt.figure().clear() # clears all graphs from previous input.
      while True:
          try:
              answer = int(input("graph equation, plot points, simple equation solver(one variable x), graph multiple, or surface plot? (1,2,3,4,5): "))
              if answer == 1:
                  break
              elif answer == 2:
                  break
              elif answer == 3:
                  break
              elif answer == 4:
                  break
              elif answer == 5:
                break
          except ValueError:
              answer = 0
              print("invalid syntax: 1,2,3 or 4")
      if answer == 2:
          b = []
          d = []
          leftBound = int(input('Input Leftbound: '))
          rightBound = int(input('Input Rightbound: ')) # these two are useless for plotting points but if a try and substitute them for other numbers it breaks so we just gonna keep it.
          amt = int(input('amount of data: '))
          for i in range(amt):
              b.append(int(input("Enter X: ")))
              d.append(int(input("Enter Y: ")))
          fig = px.scatter(x=b,y=d,trendline='ols')
          fig.show()
      elif answer == 1: 
          plt.figure().clear() 
          leftBound = int(input("Enter LeftBound: "))
          rightBound = int(input("Enter RightBound: "))
          userEq = input("Enter Equation: y = ")
          graph(userEq, range(leftBound, rightBound))
      elif answer == 3:
          while True:  
              userEq = input("Enter Equation y = ")
              xval = input("Enter x value: ")
              userEq = userEq.replace("x", xval)
              try: # catch error, I know you can just do except error but don't care.
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
          color = ["r","b","g","c","m","y","w","k"] # all current supported color types
          plt.figure().clear() 
          amt = 0 # placeholder
          amt = int(input("How many graphs? (max of 8): "))
          if amt > 8:
              while amt > 8:
                  amt = int(input("How many graphs? (max of 8): "))
          leftBound = int(input("Enter LeftBound: "))
          rightBound = int(input("Enter RightBound: "))
          upperBound = int(input("Enter UpperBound: "))
          lowerBound = int(input("Enter LowerBound: "))
          for i in range(amt):
              tempColor = color[0] # gets the first color in the list
              userEq = input("Enter Equation: y =")
              graph2(userEq, range(leftBound,rightBound),tempColor,lowerBound,upperBound)
              color.pop(0) #removes the first color in the list.
          plt.show()
      elif answer == 5: 
          x = np.arange(float(input("Number 1 (-): ")), float(input("Number 2 (+): ")), float(input("Number 3 (interval): ")))
          y = np.arange(float(input("Number 4 (-): ")), float(input("Number 5 (+): ")), float(input("Number 6 (interval): ")))
          
          surface(x,y)
          plt.show()