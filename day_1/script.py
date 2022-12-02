import numpy as np

total_calories = 0
elves_inventories = []

with open("input.txt", "r") as data:
    for line in data:
        if line != "\n":
            total_calories += int(line)
        else:
            elves_inventories.append(total_calories)
            total_calories = 0

sorted_inventories = np.sort(elves_inventories)
print(np.sum(sorted_inventories[-3:]))
