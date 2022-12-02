import numpy as np

input = open("input.txt", "r")

total_calories = 0
elves_inventories = []
for line in input:
    if line != "\n":
        total_calories += int(line)
    else:
        elves_inventories.append(total_calories)
        total_calories = 0

sorted_inventories = np.sort(elves_inventories)
print(np.sum(sorted_inventories[-3:]))
