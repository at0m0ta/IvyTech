
'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 5.13
    
    02/10/2018
    
    '''
# 5.13 Find numbers divisible by 5 or 6 but not both

x = 1
# x will keep count

for genNum in range(100, 201):
#this gives the range of numbers (100 - 200) that we will be working in
    
    if genNum % 5 == 0 or genNum % 6 == 0:
# if the generated number (genNum) gives a remainder of 0 when divided by 5 or 6...
        if x % 10 != 0:
# if the counter's remainder is not 0...
            print(genNum, end = " ")
# then print the genNum and place a space (" ") at the end
        else:
            print(genNum)    
# else, if x divided by 10 gives a remainder of 0 then just print the genNum

        x += 1
#this adds 1 to our counter (x) as we go through the loop
