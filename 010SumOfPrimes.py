# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from datetime import datetime
from math import sqrt

starttime = datetime.now()

maxPrime = 2000000
sumPrimes = 0
numbers = [1] * maxPrime

# "Sieve of Eratosthenes" (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode):
for i in range(2,int(sqrt(maxPrime + 1)) + 1):
    if numbers[i] == 1:
        for j in range(0, maxPrime + 1):
            k = i * i + i * j

#            print i, "^2 =",i * i,";", i, "*", j, "=", i * j, "; k =",i * i + i * j

            if k > maxPrime - 1:
                break
            else:
                numbers[k] = 0

print "Sieve Execution time:", datetime.now() - starttime

for i in range(2, maxPrime):
    if numbers[i] == 1:
        sumPrimes += i
#        sumPrimes = sumPrimes + i

print "Sum of all Primes less than", maxPrime,"is",sumPrimes
print "Execution time:", datetime.now() - starttime

