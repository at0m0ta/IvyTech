'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M02 Programming Assignment 3.11
    
    01/27/2018
    
    '''

#3.11 Reverse number

n = input("Enter an integer: ") [::-1]

'''
    The -1 lets the program know you want to start at the very last character in the string.
    The :: lets the program know to keep going down the string and list every character in
    the -1 position
'''


print("The reversed number is: %s" % n)

'''
    %s becomes a placeholder and passes the % value to string variable n
    
'''
