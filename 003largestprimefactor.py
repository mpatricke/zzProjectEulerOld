# Project Euler problem 003 https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
#
#       2520 = 2^3 x 3^2 x 5^1 x 7^1
#        504 = 2^3 x 3^2       x 7^1
#        245 =             5^1 x 7^2

from datetime import datetime

starttime = datetime.now()

target = 2520
maxPrime = target
primArr = {}
qpDiv = 2

while qpDiv * qpDiv <= maxPrime:

    powPrime = 0
    while maxPrime % qpDiv == 0:
        powPrime += 1
        primArr[qpDiv] = powPrime
        maxPrime /= qpDiv

    qpDiv += 1

if maxPrime > 1:
    primArr[maxPrime] = 1

primSort = sorted(primArr)
lenPrimSort = len(primSort)

print
print "The prime factors of",('{:,}'.format(target)),"are:"
for i in range(0,lenPrimSort):
    print ('{:>12}{:>3}{:<8}{:>3}{:>12}'.format(primSort[i], " ^ ", primArr[primSort[i]]," = ",primSort[i]**primArr[primSort[i]]))
print "Execution time:", datetime.now() - starttime