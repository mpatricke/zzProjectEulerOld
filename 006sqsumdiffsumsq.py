#006 diff of sum of squares and square of sum
sumsq = 0
sqsum = 0
sqn = 0
smsqdiffsqsum = 0
for n in range(1, 101):
    sqn = n * n
    sumsq = sumsq + sqn
    sqsum = sqsum + n
sqsum = sqsum * sqsum
smsqdiffsqsum = sqsum - sumsq
print(n)
print(sqsum)
print(sumsq)
print(smsqdiffsqsum)
