'''
Liliana Varela
M10 15.2
04/08/2018
'''

#15.4 Sum series
def main():
    #we set the the list to print 10 numbers starting with one
    for i in range(1, 10 + 1):
        print(i, Sum(i))


def Sum(i):
    #if index is 1 then return 1
    if i == 1:
        return 1
    else:
        #this is the recursive call, index minus 1 plus 1.0 divided by 1
        return m(i - 1) + 1.0 / i
main()
