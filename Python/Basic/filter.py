from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,0]

even = list(filter(lambda n : n % 2 == 0, nums))
doubles = list(map(lambda n : n * 2, even))
sum = reduce(lambda a, b : a + b, doubles)

print(doubles)
print(even) 
print(sum)