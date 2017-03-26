# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers

from datetime import datetime

starttime = datetime.now()

maxNo = 1000
minNo = 99
maxPalindrome = 0
maxx = 0
maxy = 0

for x in range(maxNo, minNo, -1):

    for y in range(maxNo - 1, x - 1, -1):

        qPalindrome = x * y

        if qPalindrome < maxPalindrome:
            break

        strqp = str(qPalindrome)
        lenqp = len(strqp)

        for i in range (1, int(lenqp / 2) + 1):
            if strqp[i - 1] != strqp[lenqp - i]:
                break
            else:
#                print x, y, qPalindrome, strqp, lenqp, i, strqp[i - 1], strqp[lenqp - i]
                if i == int(lenqp / 2):
#                    print "Next palindrome = ", qPalindrome, x, y

                    if qPalindrome > maxPalindrome:
                        maxPalindrome = qPalindrome
                        maxx = x
                        maxy = y
#                        print "Max Palindrome = ", maxx, "x", maxy, "=", maxPalindrome

print "Max Palindrome = ",maxx, "x",maxy,"=", maxPalindrome
print "Execution time:", datetime.now() - starttime