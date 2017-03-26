#
# # get the sum x of all numbers less than nmax that are
# divisible without remainder by 3 or by 5
x = 0
nmax = 1000000
for n in range(1, nmax):
    if n % 3 == 0:
        x = x + n
    else:
        if n % 5 == 0:
            x = x + n
print(x)