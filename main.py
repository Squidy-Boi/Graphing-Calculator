#import stuffff here
import complex
from calculator import calculatorReal
import math
from Graphing import graphing
#this is the intro where it will let the user which stuff they want to use

print("TE 1\nEasily one of the Calculators\nV1.0")
print("Which Function would you like to use")
whichMode = input("1: equation solver 2: complex number calculator\n3: graphing 4: calculator 5: end\n").lower()

#checks user input to determine which function to use
def functionChooser(mode):
  if mode == "graphing" or mode == "3":
    graphing()
  elif mode == "equation solver" or mode== "1":
    print("still needs to be created")
  elif mode == "complex number calculator" or mode == "2":
    print("still needs to be created")
  elif mode == "calculator" or mode == "4":
    calculatorReal()
  else:
    mode=input("input a valid function:\n").lower()
    functionChooser(mode)
functionChooser(whichMode)

#secondary function that gets called at the end of the users time with other funcitons
def returning():
  whichMode = input("1: equation solver 2: complex number calculator\n3: graphing 4: calculator 5: end\n").lower()
  functionChooser(whichMode)
