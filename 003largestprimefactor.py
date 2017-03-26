# Project Euler problem 003 https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from datetime import datetime
from math import sqrt

starttime = datetime.now()

#                       # fwd   reverse     stackover   my run time
#target = 13195         #  29        29            29     0.000932"
target = 675143        #  43        43          2243     0.0176"
# target = 6475143       #2417      2417          2417     0.0139"
# target = 61475143      #   1  61475143...   61475143     1.302"
# target = 651475143     #  11        11        731173    13.258"
# target = 6851475143    #-- no run --      6851475143
# target = 60851475143   #-- no run --     60851475143
# target = 600851475143  #-- no run --            6857


#solution found on stackoverflow:
maxprime = target
qpdiv = 2
while qpdiv * qpdiv < maxprime:
    while maxprime % qpdiv == 0:
        maxprime = maxprime / qpdiv
    qpdiv = qpdiv + 1
    print('qpdiv:',qpdiv,"maxprime:",maxprime)

print("(stackeoverflow) the largest prime factor of ",target," is ",maxprime)
print datetime.now() - starttime

#Magnus's code: this all works, mostly, sort of :
#starttime = datetime.now()
#qprime = 1
#primes = range (1, int(target / 250))      #runs for ever
#primes = range (1, int(sqrt(target)))      #!!!excludes possible max prime!!!

#for qprime in range(len(primes)-1,1,-1):   #reverse
#for qprime in range(3,len(primes)-1):      #forward
#    primes[qprime] = 1
#
#    for idx in range(2, qprime):
#        print("now evaluating qprime:",qprime,"idx:",idx)
#
#        if qprime % idx == 0:
#            primes[qprime] = 0
#            break
#
#    if primes[qprime] == 1:
#        if target % qprime == 0:
#            maxprime = qprime
#            print("maxprime",maxprime)
#            break                          #reverse only
#
#print("(my code)the largest prime factor of ",target," is ",maxprime)
#print datetime.now() - starttime
