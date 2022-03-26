from functools import reduce

numbers = [1, 2, 3, 4, 5]

def reducer(acc, val):
    return acc+val

print(reduce(sum, numbers, 10))