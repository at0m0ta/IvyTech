'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Assignment 3.1
    
    01/27/2018
    
    '''
# 3.1 Geometry: area of a pentagon

import math

r = eval(input("Enter the the length from the center of the pentagon to the vertex: "))
s = (2 * r) * math.sin( math.pi / 5)
a = (3 * math.sqrt(3)) / 2 * (math.pow(s, 2))

print("The area of the pentagon is: ", format(a, "<10.2f"))
