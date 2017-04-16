# https://projecteuler.net/problem=18
# https://projecteuler.net/problem=67
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 3 + 7 + 4 + 9 = 23:
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# core solution based on http://code.jasonbhill.com/python/project-euler-problem-18/

from datetime import datetime
import operator

starttime = datetime.now()

def recSumAtRow(rowData, rowNum):                      # define a recursive function to create partial sums by row
    for i in range(len(rowData[rowNum])):              # iterate over the given row
        rowData[rowNum][i] += max([rowData[rowNum + 1][i], rowData[rowNum + 1][i + 1]])

    if len(rowData[rowNum]) == 1:
        return rowData[rowNum][0]
    else:
        return recSumAtRow(rowData, rowNum - 1)

rowData = []
rowSums = []
rowCount = maxSumNext = idxMaxNext = 0

#with open('018LargeSumTestDat') as dataFile:
with open('018LargeSumDat') as dataFile:
#with open('067LargeSumDat') as dataFile:
    for line in dataFile:
        rowCount += 1
        rowSums.append([int(i) for i in line.rstrip('\n').split(" ")])
        rowData.append([int(i) for i in line.rstrip('\n').split(" ")])

result = recSumAtRow(rowSums, len(rowSums) - 2)         # start at second to last row

print
print "Current Line:         | Next Line:"
print "No.   Idx   Sum  Data | No.   Idx   Sum  Data"
print "====  ===   ===  ==== | ====  ===   ===  ===="

for i in range(0,rowCount):                             # now trace back *from the top* through the data for the path
    idxMax = idxMaxNext

    if i < rowCount - 1:                                # until the second last line
        if i == 0:                                      # determine the running max sum on the current line
            sumMaxVal = result
        else:
            sumMaxVal = maxSumNext

        maxSumNext = max(rowSums[i + 1][idxMax],rowSums[i + 1][idxMax+1]) # find the max of the two sums below ...

        if maxSumNext == rowSums[i + 1][idxMax]:        # ... and thus the index of the max sum below
            idxMaxNext = idxMax
        else:
            idxMaxNext = idxMax + 1

        maxValLineNext = rowData[i+1]                   # read the *next* line of raw data ...
        maxValNext = maxValLineNext[idxMaxNext]         # ... and required data is at the same index

        print ('{:>4} {:>4} {:>5} {:>5} {:>1} {:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, sumMaxVal, rowData[i][idxMax], "|", i + 1, idxMaxNext, maxSumNext, maxValNext))

    else:
        print ('{:>4} {:>4} {:>5} {:>5}'.format(i, idxMax, maxSumNext, rowData[i][idxMax])), "|   --- end of data ---"

print
#print rowData
print "Maximum path sum =", result, "; found in:", datetime.now() - starttime, "secs."
