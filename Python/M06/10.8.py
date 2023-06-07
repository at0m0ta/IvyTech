'''
Liliana Varela-Rodriguez
04/11/2018
M06 Programming Excises 10.08
'''
#10.8 Find the index of the smallest element

def main():
    #input number
    i = input("Enter numbers, seperate with ( space ) : ")
    #takes string of numbers
    items = i.split()
    #turn string into integers
    numbers = [ eval(x) for x in items ]
    #get smallest number 
    print("The smallest number in the list is: ", indexOfSmallestElement(numbers))
    
#get the smallest number
def indexOfSmallestElement(list): 
    #setting up minimum of list sub
    min = list[0]
    #setting MyIndex to 0
    minIndex = 0
    #setting up k to go through each number in list
    for k in range(1, len(list)): 
        #if the minimum is greater than the list sub...
        if min > list[k]: 
            #then make the minimum equal the list sub... 
            min = list[k] 
            #and MyIndex equal to k, the subnumber  
            minIndex = k
        
    return minIndex

main()