from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
product = reduce(lambda x, y: x * y, nums)

print("Squared:", squared)
print("Even:", even)
print("Product:", product)