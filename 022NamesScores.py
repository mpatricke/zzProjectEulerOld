# https://projecteuler.net/problem=22
#
# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

from datetime import datetime

def nameValCalc(name):
    nameValue = 0
    for i in range(0,len(str(name))):
        nameValue += alphaData.index(name[i])
    return nameValue

starttime = datetime.now()

alphaData = ["$","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nameValTot = 0

#nameFile = open('p022_namesMagnus.txt', 'rU')
#nameFile = open('p022_namesFam.txt', 'rU')
nameFile = open('p022_names.txt', 'rU')

nameData = sorted(nameFile.read().replace('"', '').rstrip('\n').split(','), key=str)

for i in range (1, len(nameData)+1):
    nameValTot += nameValCalc(nameData[i-1]) * i

print
print "The sum of the name values is:", nameValTot, ", found in:", datetime.now() - starttime, "secs."