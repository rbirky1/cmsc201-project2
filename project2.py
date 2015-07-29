# File:   project2.py
# Author: Rachael Birky
# Date:   05.07.12
# Section:02
# This program simulates auto-fill using recursion.


import sys
import string

# printGreeting() displays a greeting and explanation of program
# input: none
# output: none
def printGreeting():
    print "\nWelcome!  This program simulates auto-fill using recursion.\n\
Please remember to supply a file and a valid x and y coordinate."

# makeMatrix() creates a matrix of the appropriate size, fills it with
#  content of file
# input: a file
# output: a matrix
def makeMatrix(inFile):

    # Read first line, strip whitespace
    # The length of this line is equivalent to the number of columns
    colCount = len(inFile.readline().strip())

    # Count number of lines
    # This is equivalent to the number of rows
    inFile.seek(0)
    rowCount = 0
    for line in inFile:
        rowCount += 1

    # Create empty matrix of appropriate size
    fileMatrix = [[' ' for i in range(colCount)] for j in range(rowCount)]

    # Fill matrix with content of file
    inFile.seek(0)
    for row in range(rowCount):
        thisString = inFile.readline()
        for char in range(colCount):
            fileMatrix[row][char] = thisString[char]
    
    return fileMatrix, rowCount, colCount

# printMatrix() displays the given matrix to the screen
# input: a matrix
# output: none (print statements)
def printMatrix(aMatrix):

    for row in aMatrix:
        for char in row:
            print char,
        print

# autoFill() is a recursive function that calls itself to fill the matrix
#  with a certain character until the base case is met
# input: matrix, x and y coordinates, number of rows and columns
# output: modified matrix
def autoFill(aMatrix, xCoor, yCoor, rowCount, colCount):

    # Base case: when an actual boundary or natural boundary is reached
    # Some white space of code removed to be closer to 80 characters in length
    if (xCoor<0) or (xCoor>=rowCount) or (yCoor<0) or (yCoor>=colCount) or aMatrix[xCoor][yCoor]=="x":
        return
    else:
        # Change current character to 'x'
        aMatrix[xCoor][yCoor] = "x"

        # Call function for each character below...
        autoFill(aMatrix, xCoor+1, yCoor, rowCount, colCount)
        # above...
        autoFill(aMatrix, xCoor-1, yCoor, rowCount, colCount)
        # left...
        autoFill(aMatrix, xCoor, yCoor-1, rowCount, colCount)
        # and right of current character.
        autoFill(aMatrix, xCoor, yCoor+1, rowCount, colCount)

    return aMatrix

# writeTFile() saves the output of autoFill() in a file (matrix1-results.txt)
# input: aMatrix
# output: none (writes to file)
def writeToFile(aMatrix, fileName):

    # Create new name for file
    newFileName = fileName + "-results.txt"

    # Open file and write row of matrix
    #  by concantenating each character to a string
    #  and writing string to file as a line
    outFile = open(newFileName, "w")
    for row in aMatrix:
        matrixRow = ""
        for char in row:
            matrixRow += char
        outFile.write(matrixRow+"\n")
        
    return newFileName

def validCoor(xCoor, yCoor, rowCount, colCount):

    return xCoor >= 0 and xCoor <= rowCount and yCoor >= 0 and yCoor <= colCount

def main():

    printGreeting()

    # The following is adapted from...
    # Zelle, John M. Python Programming:
    #  An Introduction to Computer Science. Wilsonville, Or.: Franklin,
    #  Beedle, 2004. 214-17. Print.
    try:
        inFile = open(sys.argv[1], "r")
    except:
        print "**You must supply a valid document**"
        sys.exit()

    # Check for numerical coordinates given
    try:
        xCoor = int(sys.argv[2])
        yCoor = int(sys.argv[3])
    except:
        print "\n*You must provide numerical coordinates\
Please try again.\n*"
        sys.exit()

    # File name, without extension
    fileName = sys.argv[1][:-4]

    # Create matrix of original file by calling makeMatrix
    fileMatrix, rowCount, colCount = makeMatrix(inFile)

    # Make sure coordinates are inbounds
    # If so, print original matrix to screen and results to screen and file
    if validCoor(xCoor, yCoor, rowCount, colCount):

        print "\nMatrix BEFORE autofill"
        printMatrix(fileMatrix)

        newMatrix = autoFill(fileMatrix, xCoor, yCoor, rowCount, colCount)

        print "\nMatrix AFTER autofill, starting at %d, %d" % (xCoor, yCoor)
        printMatrix(newMatrix)
        newFileName = writeToFile(newMatrix, fileName)
    
        print "\nThis image can be found in " + newFileName
        print
    else:
        print "\n*Coordinates out of bounds. Please try again.*\n"
    
main()
