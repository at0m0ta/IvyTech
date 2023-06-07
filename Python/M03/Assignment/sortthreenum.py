'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 6.5
    
    02/10/2018
    
    '''
# 6.5 Sort three numbers
def main():
    num1, num2, num3 = eval(input("Enter 3 numbers seperate with ( , ): "))
    list = num1, num2, num3             #gathering numbers in a  list that
                                        #will be sorted

    displaySortedNumbers(list)          #calling displaySortedNumbers 

def displaySortedNumbers(list):
        print(sorted(list, key=float, reverse=False))
    
                                            #reverse sorting function
                                            #that is able to catch floating
                                            #numbers
main()
