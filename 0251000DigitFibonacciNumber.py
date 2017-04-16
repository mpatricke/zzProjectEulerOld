# https://projecteuler.net/problem=25
#
# The Fibonacci sequence is defined by the recurrence relation:
#    F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1
#
# Hence the first 12 terms will be:
#    F1=1; F2=1; F3=2; F4=3; F5=5; F6=8; F7=13; F8=21; F9=34; F10=55; F11=89; F12=144
#
# The 12th term, F12, is the first term to contain three digits. What is the index of the first term
# in the Fibonacci sequence to contain 1000 digits?

from datetime import datetime

starttime = datetime.now()

fibRunTot = tarLen = 1000
fibSeq = [1, 1]
i = 3

while len(str(fibRunTot)) < tarLen:
    fibRunTot = fibSeq[i - 2] + fibSeq[i - 3]
    fibSeq.append(fibRunTot)
    i += 1

print
print "The", i-1, "th Fibonacci number is the first to have a length of", len(str(fibRunTot)), "digits."
print "The number is", fibRunTot
print "Found in:", datetime.now() - starttime, "secs."