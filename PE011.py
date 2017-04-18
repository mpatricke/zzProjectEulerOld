# https://projecteuler.net/problem=11
#
# In the 20 x 20 grid 011LargeGrid.txt, the product along the diagonal 26 x 63 x 78 x 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20 x 0 grid?

from datetime import datetime
import os

starttime = datetime.now()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

adjNoCount = 4
rowData = []
numSeq = [0]*adjNoCount
rowCount = rowLen = maxProd = iMax = jMax = prodNxt = 0 

#with open('011LargeGridTest.txt') as dataFile:
with open('011LargeGrid.txt') as dataFile:
    for line in dataFile:
        rowCount += 1
        rowData.append([int(i) for i in line.rstrip('\n').split(" ")])

rowLen = len(rowData[rowCount-1])

for i in range(0,rowLen):
    for j in range (0,rowCount-(adjNoCount-1)):
        prodNxt = rowData[i][j] * rowData[i][j+1]*rowData[i][j+2]*rowData[i][j+3]
        if prodNxt > maxProd:
			maxProdDir = "right"
            maxProd = prodNxt
            iMax = i
            jMax = j
			numSeq = [rowData[i][j],rowData[i][j+1],rowData[i][j+2],rowData[i][j+3]]

	if i < rowLen-(adjNoCount-1):
		for j in range (0,rowCount):
			prodNxt  = rowData[i][j] * rowData[i+1][j]*rowData[i+2][j]*rowData[i+3][j]
			if prodNxt > maxProd:
				maxProdDir = "down"
				maxProd = prodNxt
				iMax = i
				jMax = j
				numSeq = [rowData[i][j],rowData[i+1][j],rowData[i+2][j],rowData[i+3][j]]

			if j < rowCount - adjNoCount:
				prodNxt  = rowData[i][j] * rowData[i+1][j+1]*rowData[i+2][j+2]*rowData[i+3][j+3]
				if prodNxt > maxProd:
					maxProdDir = "diagonally leading"
					maxProd = prodNxt
					iMax = i
					jMax = j
					numSeq = [rowData[i][j],rowData[i+1][j+1], rowData[i+2][j+2],rowData[i+3][j+3]]

			if j > adjNoCount -1:
				prodNxt  = rowData[i][j] * rowData[i+1][j-1]*rowData[i+2][j-2]*rowData[i+3][j-3]
				if prodNxt > maxProd:
					maxProdDir = "diagonally trailing"
					maxProd = prodNxt
					iMax = i
					jMax = j
					numSeq = [rowData[i][j],rowData[i+1][j-1],rowData[i+2][j-2],rowData[i+3][j-3]]

print
print "The maximum product of any",adjNoCount,"adjacent numbers in the",rowLen,"x",rowCount," array is",maxProd
print
print "Starting",maxProdDir,"from cell", iMax+1,",", jMax+1,": the product of", numSeq
print
print "Execution time:", datetime.now() - starttime