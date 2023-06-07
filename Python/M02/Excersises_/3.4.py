'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 3.4
    
    01/27/2018
    
    '''
# 3.4 Geometry: area of a pentagon

import math

n = eval(input("Enter the number of sides on the polygon: "))
s = eval(input("Enter the length of a side: "))

area = (n * math.pow(s,2)) / (4 * math.tan(math.pi / n))

print("The area of the polygon is ", area)

# my answer seems off by 1. it maybe the way I decided to write the formula
