'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M01 Programming Exercises 2.2
    
    01/28/2018
    
    '''

# 2.2 Compute the volume of a cylinder

radius, length = eval(input("Enter the radius and length of the cylinder. Seperate with comma "))
area = radius * radius * 3.14159
volume = area * length
print("area = ", area, "volume = ", volume)

