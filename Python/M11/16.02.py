'''
Liliana Varela-Rodriguez
M11 16.2
04/15/2018
'''
#16.2 Maximum increasing ordered subsequence 
def main():
    #seperating the characters entered at the input
    s = input("Enter a string: ").strip()
    #output
    print("Maximum consecutive substring is " + maxSubstring(s))

# The worst-case complexity is O(n^2)
def maxSubstring(s):
    # maxLength[i] stores the length of the max substring ending at index i
    maxLength = len(s) * [0]
    # previous[i] stores the index of the previous element in the sequenece
    previous = len(s) * [0]

    #i = the previous character in the string
    for i in range(len(s)):
      previous[i] = -1
      
      for j in range(i - 1, -1, -1):
          #if the first character is greater than the second character
          #and the there are more of the second character than there are of the first
          #then maxlenght = the second character and the character(previous) is replaced
          #with the second character also.
        if s[i] > s[j] and maxLength[i] < maxLength[j] + 1:
          maxLength[i] = maxLength[j] + 1
          previous[i] = j

    # maxL is the character that is greater in value and repeats the most often
    maxL = maxLength[0]
    index = 0
    for i in range(1, len(s)):
        #if the character that repeats the most is greater than the a previous character
        #then switch the characters within the string until the list is less than 0 
        if maxL < maxLength[i]:
            maxL = maxLength[i]
            index = i


    # chars = listing the maxL characters in list in sequential order or the above comparison
    chars = (maxL + 1) * [0]
    #set i to equal the maxL
    i = maxL
    while index != -1:
        #While not below 0, set chars[i] to equal the s[index] list 
         chars[i] = s[index]
         #go down the list and update index to equal what you have already checked in the index
         i -= 1
         index = previous[index]

    return str(chars) #this returns the string of characters in the order listed in chars 

main()
