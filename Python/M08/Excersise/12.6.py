'''
Liliana Varela-Rodriguez
M08 Chapter 12
Exercise 12.2
'''

#12.2 The location class

#creating location class with its data fields
class Location:
    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue
    #methods to retrieve data
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getMaxValue(self):
        return self.maxValue
    
    
def main():
    #getting columns and rows from user
    row, column = eval(input("Enter the number of rows and columns in the list, seperated by comma: "))

    matrix = []
    
    #for rows
    for i in range(row):
        s = input("Enter numbers for row " + str(i) + " : ")
        #seperating numbers into individual strings
        items = s.split()
        #converting strings to numbers
        list = [ eval(x) for x in items ]
        matrix.append(list)

    # setting location to the largest value within the matrix
    location = locateLargest(matrix)
    #printing information
    print("The largest element = "
          + str(location.getMaxValue()) + " Located at: ("
          + str(location.getRow()) + ", " + str(location.getColumn()) + ")")

#locating max value
def  locateLargest(a):
    #maxValue is set to matrix a [row] [column]
    maxValue = a[0][0]
    #values of row and column
    row = 0
    column = 0
    #i is length of matrix a 
    for i in range(len(a)):
        #j is length of matrix a's rows
        for j in range(len(a[i])):
            #if the maxValue is less than the current "cell" of matrix a
            if maxValue < a[i][j]:
                #then the maxValue equals the current "cell" of matrix a
                maxValue = a[i][j]
                row = i
                column = j
    #returning location information
    return Location(row, column, maxValue)

main()
