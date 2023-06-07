'''
Liliana Varela-Rodriguez
04/01/2018
M09 13.5
'''

#13.5 Replace the Text

def main():
    #input file name 
    file1 = input("Enter a filename: ").strip()
    #replacing string in old file
    oldline = input("Enter the string to replace: ")
    #new string to be used 
    newline = input("Enter the new string to replace the old string: ")

    #opening file one 
    infile = open(file1, "r")

    lst = []

    #replacing line in file
    for line infile:
        changed = line.replace(oldline, newline)
        lst.append(changed)
    #closing file
    infile.close()

    #Copy contents of array to file
    outfile = open(file1, "w")
    for line in lst:
        outfile.write(line)

    #Closing
    outfile.close()
    print("Done")

main()
