## WAP To import an external text file into Python
# 1. Create/Find your text file
# 2. Create a variable to store your file, use the open() function to store your file ex. open("test.txt")
# 3. Create a variable to store the file data and use the variable of the file (externalFile) and open it with .read()
# 4. Create a print function to print the data

## Cursor Manner = Read method uses the cursor manner, it reads the file byte by byte and stays at the last position of the first function (If you add parameters to the .read function)

externalFile = open("test.txt")

# fileContent = externalFile.read()
# print(fileContent) 

# How .readlines() function works
# .readlines() will read all the lines in the file and return a list

# fileContent = externalFile.readline() #will return the first line of the file
# print(fileContent)

fileContent = externalFile.readlines() #will return a list
print(fileContent)
    
# Once we have list of all the lines, we can loop over through them to extract every line individually
# Run a for loop that will go through the entire index and return all the data in the file

for index in range(len(fileContent)): # 0, 1, 2, 3, 4
    everyline = fileContent[index]
    print(everyline)