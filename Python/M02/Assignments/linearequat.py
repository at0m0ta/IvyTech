'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Exercises 4.3
    
    01/27/2018
    
    '''
# 4.3 Algebra: solve 2 x 2 linear equations

a, b, c, d, e, f = eval(input("Enter six integers a, b, c, d, e, f: "))

x = (e * d) - (b * f) / (a * d) - (b * c)
y = (a * f) - (e * c)) / ((a * d) - (b * c)

if (a * d) - (b * c) == 0:
    print("Equation has NO solution")
elif e == (a * x) + (b * y) and f == (c * x) + (d * y):
    print("x is: ", x, " and y is ", y)
else:
    print("Equation has NO solution")
