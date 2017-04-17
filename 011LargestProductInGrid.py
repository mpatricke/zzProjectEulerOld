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
rowCount = rowLen = 0
maxProd = iMax = jMax = 0
prodRt = maxProdRt = iMaxRt = jMaxRt = 0
prodDn = maxProdDn = iMaxDn = jMaxDn = 0
prodDL = maxProdDL = iMaxDL = jMaxDL = 0
prodDT = maxProdDT = iMaxDT = jMaxDT = 0

#with open('011LargeGridTest.txt') as dataFile:
with open('011LargeGrid.txt') as dataFile:
    for line in dataFile:
        rowCount += 1
        rowData.append([int(i) for i in line.rstrip('\n').split(" ")])

rowLen = len(rowData[rowCount-1])

for i in range(0,rowLen):
    for j in range (0,rowCount-(adjNoCount-1)):
        prodRt = rowData[i][j] * rowData[i][j+1]*rowData[i][j+2]*rowData[i][j+3]
        if prodRt > maxProdRt:
            maxProdRt = prodRt
            iMaxRt = i
            jMaxRt = j

for i in range(0,rowLen-(adjNoCount-1)):
    for j in range (0,rowCount):
        prodDn  = rowData[i][j] * rowData[i+1][j]*rowData[i+2][j]*rowData[i+3][j]
        if prodDn > maxProdDn:
            maxProdDn = prodDn
            iMaxDn = i
            jMaxDn = j

        if j < rowCount - adjNoCount:
            prodDL  = rowData[i][j] * rowData[i+1][j+1]*rowData[i+2][j+2]*rowData[i+3][j+3]
            if prodDL > maxProdDL:
                maxProdDiL = prodDL
                iMaxDL = i
                jMaxDL = j

        if j > adjNoCount -1:
            prodDT  = rowData[i][j] * rowData[i+1][j-1]*rowData[i+2][j-2]*rowData[i+3][j-3]
            if prodDT > maxProdDT:
                maxProdDT = prodDT
                iMaxDT = i
                jMaxDT = j

maxProd = max(maxProdRt, maxProdDn, maxProdDL, maxProdDT)

if maxProd == maxProdRt:
    iMax = iMaxRt
    jMax = jMaxRt
    maxProdDir = "right"
    numSeq = [rowData[iMax][jMax],rowData[iMax][jMax+1],rowData[iMax][jMax+2],rowData[iMax][jMax+3]]

else:
    if maxProd == maxProdDn:
        iMax = iMaxDn
        jMax = jMaxDn
        maxProdDir = "down"
        numSeq = [rowData[iMax][jMax],rowData[iMax+1][jMax],rowData[iMax+2][jMax],rowData[iMax+3][jMax]]

    else:
        if maxProd == maxProdDL:
            iMax = iMaxDL
            jMax = jMaxDL
            maxProdDir = "diagonally leading"
            numSeq = [rowData[iMax][jMax],rowData[iMax+1][jMax+1], rowData[iMax+2][jMax+2],rowData[iMax+3][jMax+3]]

        else:
            iMax = iMaxDT
            jMax = jMaxDT
            maxProdDir = "diagonally trailing"
            numSeq = [rowData[iMax][jMax],rowData[iMax+1][jMax-1],rowData[iMax+2][jMax-2],rowData[iMax+3][jMax-3]]

print
print "The maximum product of any",adjNoCount,"adjacent numbers in the",rowLen,"x",rowCount," array is",maxProd
print
print "Starting",maxProdDir,"from cell", iMax+1,",", jMax+1,": the product of", numSeq
print
print "Execution time:", datetime.now() - starttime