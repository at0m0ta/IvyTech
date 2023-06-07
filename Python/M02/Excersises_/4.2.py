'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 4.2
    
    01/27/2018
    
    '''
# 4.2 Game: add three numbers

import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)


answer = eval(input("What is " + str(num1) + " + " \
                    + str(num2) + " + " + str(num3) + " ? "))

print(num1, " + ", num2, " + ", num3, " = ", answer, "is ...")

print(num1 + num2 + num3 == answer)
