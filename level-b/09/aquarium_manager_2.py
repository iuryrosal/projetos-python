import json

f = open("aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def move_fishes_to_aquarium_42(animal):
    if animal["type"] == "fish":
        animal["tank number"] = 42
    return animal

print(list(map(move_fishes_to_aquarium_42, animals)))