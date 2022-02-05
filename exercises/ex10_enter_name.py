import random

names = []

while len(names) < 8:
    name = input("Enter names: ")
    names.append(name)

print(random.choice(names))