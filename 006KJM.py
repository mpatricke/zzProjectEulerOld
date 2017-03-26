numbers = range(1, 101)
print "{:,}".format(sum(numbers) ** 2 - sum([x ** 2 for x in numbers]))