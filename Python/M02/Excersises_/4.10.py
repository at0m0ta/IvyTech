'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 4.10
    
    01/27/2018
    
    '''
# 4.10 Game: multiplication quiz

import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = eval(input("What is " + str(num1) + " * " + str(num2) + "? "))

print(num1, " * ", num2, " = ", answer, " is ", num1 * num2 == answer)
