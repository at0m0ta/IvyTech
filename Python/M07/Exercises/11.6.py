'''
Liliana Varela
M07 Chapter 11
Programming Exercises 11.06 
'''

#11.6 Algebra: multiply two matrices
def main():
    #creating both matrix 1 and 2
    matrix1 = []
    matrix2 = []

    #for matrix1
    s = input("Enter 9 numbers, seperated by a space, that will go in a  3-by-3 matrix: ")
    #seperating items from string and removing spaces
    items = s.split()
    
    for i in range(3):
        #evaluates items and changes string into numbers
        list = [eval(items[j]) for j in range(3 * i, 3 * i + 3)]
        #appending list in matrix 1
        matrix1.append(list)

    #for matrix2
    s = input("Enter 9 numbers, seperated by a space, that will go in a  3-by-3 matrix: ")
    #seperating items from string and removing spaces
    items = s.split()
    
    for i in range(3):
        #evaluates items and changes string into numbers
        list = [eval(items[j]) for j in range(3 * i, 3 * i + 3)]
        #appending list in matrix 2
        matrix2.append(list)
        
    #creating 3rd matrix by calling on MatrixMultiplier
    matrix3 = MatrixMultiplier(matrix1, matrix2)
    #calling Results 
    Result(matrix1, matrix2, matrix3, "*")
    
#multiplying matrix 1 and 2 to create matrix 3
def MatrixMultiplier(m1, m2):
    #list is the length of m2
    list = len(m2[0]) * [0]
    #result matrix
    result = []
    #for i in the length of m1
    for i in range(len(m1)):
        #append the results for x in the list
        result.append([x for x in list])
        
    #for i in the length of results
    for i in range(len(result)):
        #for j in the length of results[0]
        for j in range(len(result[0])):
            #for k in the length of m2
            for k in range(len(m2)):
                #result plus the multiples of matrix1 and matrix2
                result[i][j] += m1[i][k] * m2[k][j]
        
    return result
          
    
#printing results
def Result(m1, m2, m3, op):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            print(" " + str(m1[i][j]), end = "")

        if i == len(m1) // 2:
            print( "  " + op + "  ", end = "")
        else:
            print( "     ", end = "")

        for j in range(len(m2[0])):
            print(" " + str(m2[i][j]), end = "")

        if i == len(m1) // 2:
            print("  =  ", end = "")
        else:
            print("     ", end = "")

        for j in range(len(m3[0])):
            print(" " + str(m3[i][j]), end = "")

        print()
        





    
main()
