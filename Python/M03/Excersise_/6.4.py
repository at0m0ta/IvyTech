'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 6.4
    
    02/10/2018
    
    '''
# 6.4 Display an integer reversed

def reverse(number):
    while number != 0:
        remainder = number % 10
        # % extracts the last number and assigns it to remainder
        print(remainder, end = "")
        # we will print the remainder first
        number = number // 10
        #and finally extract the last integer from the whole number
        #before continuing the loop
def main():
    number = eval(input("Enter any number: "))
    reverse(number)
main()

