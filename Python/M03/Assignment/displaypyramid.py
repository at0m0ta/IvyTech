'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 5.19
    
    02/10/2018
    
    '''
# 5.19 Display a pyramid

num = eval(input("Enter the number of lines from 1 - 15  "))

def as_str(i):
    s = ""
    if i <16 and i >0: s = " "
    return s + str(i)

                                                                                                                                       
allrows = ""
for j in range(1,num+2):        #for spacing                                                                                                                               
    row = " "*3*(num-j+1)

    for i in range(j-1,1,-1):   #the 1 in the middle helps position 1 at center
        s = as_str(i)           #position 1/j will begin on the right and go to
        row+=s + " "            #center 1
        
    for i in range(1,j):        #j begins on left and goes to center 1
        s = as_str(i)
        row+=s + " "
        
    row +="\n"                  #spacing for rows
    allrows +=row

print (allrows)                 #prints all the rows
