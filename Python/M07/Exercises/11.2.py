'''
Liliana Varela-Rodriguez
M07 Chapter 11
Programming Exercises 11.2
'''

#11.2 Sum the major diagonal in a matrix

def main():
    
    #create a matrix/table
    matrix = []
    
    for i in range(4):
        mtrxRows = 0
        i += 1 
        #matrix rows equal string of numbers input by user
        mtrxRows = input("Enter 4 numbers for row " + str(i) + ", seperate with a space: ")
        #seperating the items by splitting them up
        items = mtrxRows.split()
        #evaluating each item in the list and converting it to a number
        list = [ eval(x) for x in items ]
        #add them to the end of the list
        matrix.append(list)
        
    #printing statement and total of the Major Diagonal within the matrix
    print("The sum of the numbers in the major diagonal is: ", sumMajorDiagonal(matrix))
    
def sumMajorDiagonal(m):
    #sum of diagonal numbers in the matrix (m)
    sum = 0
    #for the number in the length of m (row)
    for i in range(len(m)):
        #sum plus the number in the following cell
        sum += m[i][i]
    return sum
main()
