# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#       2520 = 2^3 x 3^2 x 5 x 7

from datetime import datetime

starttime = datetime.now()

tarRange = 99
primArr = {}
runSum = 1

for i in range(1,tarRange):

    maxPrime = i
    qpDiv = 2

    while qpDiv * qpDiv <= maxPrime:

        powPrime = 0
        while maxPrime % qpDiv == 0:
            powPrime += 1
            if primArr[qpDiv] < powPrime:
                primArr[qpDiv] = powPrime
            maxPrime /= qpDiv

        qpDiv += 1

    if maxPrime > 1:
        primArr[maxPrime] = 1

primSort = sorted(primArr)
lenPrimSort = len(primSort)

for i in range(0,lenPrimSort):
    runSum *= primSort[i]**primArr[primSort[i]]

print
print "The smallest positive number that is evenly divisible "
print "by all of the numbers from 1 to", tarRange, "is:",('{:,}'.format(runSum))
print
print "Execution time:", datetime.now() - starttime