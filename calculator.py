#this can't be that bad right :clueless:
import math


def calculatorReal():
  helpChoice = input("1: help 2: calculator\n").lower()
  helpTester(helpChoice)

def helpTester(choice):
  if choice == "1" or choice == "help":
    print("help text is unnecessary")
  elif choice == "2" or choice == "calculator":
    calculator()
  else:
    choice2 = input("Please input a valid response").lower()
    helpTester(choice2)

# the plan is probably to use rsplit to seperate each part of the equation into an array and do funny math stuff with it to allow the user to create any length equations or smth stupid

def calculator():
  userEquation = input("Type equation: ")
  try:
    answer = eval(userEquation)
    repetition(answer)
  except SyntaxError:
    print("syntax error try again")
    calculator()

def calculatorAnswer(value):
  userEquation = str(value)+ input("input your equation: " + str(value))
  print(userEquation)
  try:
    answer = eval(userEquation)
    repetition(answer)
  except SyntaxError:
    print("syntax error try again")
    calculatorAnswer(value)

def repetition(value):
  continueChoice = input(str(value)+"\nDo you want to 1: continue with answer 2: continue without answer 3: stop\n").lower  
  def repetitionTester(choice):
    if choice == "1" or choice == "continue with answer":
      calculatorAnswer(value)
    elif choice == "2" or choice == "continue without answer":
      calculator()
    elif choice == "3" or choice == "stop":
      #os.execv(sys.argv[0], sys.argv)
      print("j")
    else:
      choice2 = input("Please input a valid response").lower
      repetitionTester(choice2)
  repetitionTester(continueChoice)

