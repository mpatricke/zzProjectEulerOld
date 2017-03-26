# https://projecteuler.net/problem=8
#
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 * 9 * 8 * 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

from datetime import datetime

starttime = datetime.now()

# index:           1         2
#        012345678901234567890
#TARGET = 512034506713789401034
TARGET = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
LENGTH = 13

from datetime import datetime

starttime = datetime.now()

strTarget = str(TARGET)
lenTarget = len(strTarget)
maxProd = MaxProdIndex = calcCounter = 0

for i in range(0,lenTarget - LENGTH):                      # starting from the beginning loop through all numbers

    if int(strTarget[i+LENGTH]) - 1 > int(strTarget[i]):       # if

        if int(strTarget[i]) != 0:                         # if next number = 0 don't bother

            for j in range(i,i+LENGTH-1):                  # starting at i get the number sequence

                if int(strTarget[j+LENGTH - 1]) == 0:      # if the final digit is 0 don't bothter
                    break

                else:
                    calcCounter += 1
                    tempMaxProd = 1

                    for k in range(j,j+LENGTH):
                        tempMaxProd *= int(strTarget[k])

                    if tempMaxProd > maxProd:
                        maxProd = tempMaxProd
                        maxProdIndex = j

print "Product of", LENGTH,"char series", strTarget[maxProdIndex:maxProdIndex+LENGTH],", starting at index posn",maxProdIndex, ", is",maxProd
print "Execution time:", datetime.now() - starttime, "in",calcCounter ,"calcs"