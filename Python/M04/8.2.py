'''
    Liliana Varela-Rodriguez
    
    SDEV 220 PYTHON
    
    M03 Programming Exercises 8.2
    
    02/10/2018
    
    '''
# 8.2 Check substrings

def main():                                            #input strings                                         
    s1 = input("Enter a string: ").strip()
    s2 = input("Enter a second string: ").strip()

    if hasSubString(s1, s2) != -1:                    #outputs depending on
        print(s1 + " is a substring of " + s2)    #hasSubString findings
    else:
        print(s1 + " is NOT a substring of " + s2)

def hasSubString(s1, s2):
    remainingL = len(s2)                          #remainingL will tell us how much of s2 
    i = 0;                                       #is left after it is compared with s1
                                                 # i will serve as our index
    while len(s1) <= remainingL:            # comparing lenght of s1 to s2
        if s1 != s2[i : i + len(s1)]:            #setting the range of s2 to index plus 
            i += 1                               # length of s1
            remainingL -= 1                      # add one to index and subtract 1 from remL                      
        else:
            return i
    return -1
main()
