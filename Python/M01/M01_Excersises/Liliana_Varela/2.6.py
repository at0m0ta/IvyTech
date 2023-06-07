'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M01 Programming Exercises 2.6
    
    01/28/2018
    
    '''

#2.6 Sum the digits in an integer

number = eval(input("Enter any number between 0 and 1000"))

num1 = number % 10
x = number // 10
num2 = x % 10
x = x // 10
num3 = x % 10

print("num1 + numb2 + num3 = ")
sum = num1 + num2 + num3
print(sum)
