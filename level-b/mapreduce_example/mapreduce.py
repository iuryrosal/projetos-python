import json
from functools import reduce

f = open("../aquarium_manager/aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def pick_type_animal(animals):
    return animals['type'], 1

def shuffle_types(list_animals):
    def pick_type(a):
        return a[0]
    return sorted(list_animals, key=pick_type)

def reducer(acc, val):
    if val[0] not in acc.keys():
        acc[val[0]] = 0 + val[1]
    else:
        acc[val[0]] = acc[val[0]] + val[1]
    return acc

list_types = list(map(pick_type_animal, animals))
print(list_types)
list_types_sorted = shuffle_types(list_types)
print(list_types_sorted)
quant_per_type = reduce(reducer, list_types_sorted, {})
print(quant_per_type)

