# https://projecteuler.net/problem=7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


from datetime import datetime
from math import sqrt

starttime = datetime.now()

primCount = 10001
maxPrime = primCount * 20
countPrim = 0
numbers = [1] * maxPrime
primArr = {}

# "Sieve of Eratosthenes" (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode):
for i in range(2,int(sqrt(maxPrime + 1)) + 1):
    if numbers[i] == 1:
        for j in range(0, maxPrime + 1):
            k = i * i + i * j

            if k > maxPrime - 1:
                break
            else:
                numbers[k] = 0

for i in range(1,maxPrime):
    if numbers[i] == 1:
        countPrim += 1
        primArr[countPrim - 1] = i

    if countPrim > primCount:
        break

print
print "The",countPrim - 1,"th prime number is:", primArr[countPrim - 1]
print "Execution time:", datetime.now() - starttime