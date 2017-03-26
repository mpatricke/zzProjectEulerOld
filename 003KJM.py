#target = 600851475143

target = 600851475146
x = target

div = 2
while div != x:       # for as long as div <> x
  if x % div == 0:    # if div is a divisor of x with no remainder
    print x, "divided by", div, "=",x / div,", with no remainder"
    x /= div          # set x to x divided by div
    print "x = ", x
  else:
    div += 1          #increment div by 1
#    print "div:",div, "; x:", x

print "greatest prime factor: ", x