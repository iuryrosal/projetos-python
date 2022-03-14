from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

def sum(a1, a2):
    return a1 + a2

print(reduce(sum, numbers))

print(reduce(sum, numbers, 10))
