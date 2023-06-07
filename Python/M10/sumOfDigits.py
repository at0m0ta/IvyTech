'''
Liliana Varela
M10
04/08/2018
'''
#15.1 Sum the digits in an integer using recursion

#this is the same as sumDigits
def numSum(n):
    #if n is 0 then return 0 else 
    if n == 0:
        return 0
    else:
        #using float to get first number, using modulus to get remainer (second digit) 
        return (n % 10) + numSum(n // 10)

def main():
    #entering a a number and evaluating the input
    num = eval(input("Enter an integer: "))

    print("Sum of digits in ", num, " is: ", numSum(num))

main()
