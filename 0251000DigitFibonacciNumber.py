# https://projecteuler.net/problem=25
#
# The Fibonacci sequence is defined by the recurrence relation:
#    F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1
#
# Hence the first 12 terms will be:
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144
#
# The 12th term, F12, is the first term to contain three digits. What is the index of the first term
# in the Fibonacci sequence to contain 1000 digits?

from datetime import datetime

starttime = datetime.now()

tarLen = 1000
fibSeq = []
f1 = f2 = 1
fn = fnPrev = lenFn = 0

for i in range(1,tarLen*10):
    if i == 1:
        fibSeq.append(f1)

    else:
        if i == 2:
            fibSeq.append(f2)

        else:
            fnPrev = fn
            fn = fibSeq[i-2] + fibSeq[i-3]
            fibSeq.append(fn)

    lenFn = len(str(fn))

    if lenFn >= tarLen:
        break

print "The", i, "th Fibonacci no. has a length of", lenFn, "digits, and is", fn
print "found in:", datetime.now() - starttime, "secs."


#    print "sdfg", i, fibSeq

