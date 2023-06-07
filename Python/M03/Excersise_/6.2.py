'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 6.2
    
    02/10/2018
    
    '''
# 6.2 Sum the digits in an integer

def main():
#main module : will be used to input the number
    
    number = eval(input("Enter any number: "))

    print(str("The sum of digits for ") + str(number) + str(" is ") + str(sumDigits(number)))
# printing string, number as string, and calls module sumDigits as string

def sumDigits(n):
#def sumDigits modules will add the values of our number
    temp = abs(n)
    sum = 0

    while temp != 0:
        #that while temp still has a number to extract, the loop will keep going
        
        remainder = temp % 10
        # % extracts digits (they are the remainders and will be listed using abs()
        
        sum += remainder
        #sum hold the digits gathered from remainder added together
        
        temp = temp // 10
        # gives you the floor value and will drop the last integer from temp before it is recalculated
        # within the loop
        
    return sum
#return gives you the sum

main()
