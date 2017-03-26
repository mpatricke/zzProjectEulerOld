# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
#
# ME: 2520 = 10 x 9 x 7 x 4
#          = 5 x 2 x 3 x 3 x 7 x 2 x 2
#          = 7 x 5 x 3 x 3 x 2 x 2 x 2


target = 2250
divi = 20

while target % i == 0:

#    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
# p1 x
# p2    x
# p3       x
#  4    x     x
# p5             x
#  6    x  x        x
# p7                   x
#  8    x     x           x
#  9       x                 x
# 10    x        x              x
#p11                               x
# 12    x  x  x     x                 x
#p13                                     x
# 14    x              x                    x
# 15       x     x                             x
# 16    x     x           x                       x
#p17                                                 x
# 18    x           x        x                          x
#p19                                                       x
# 20    x     x  x              x                             x

