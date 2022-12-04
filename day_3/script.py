import numpy as np


def create_backpacks_groups():
    with open("input.txt", "r") as backpacks_list:
        backpacks = backpacks_list.read().splitlines()
        return np.array_split(backpacks, len(backpacks) // 3)


def find_item(group):
    print(group)
    for item in group[0]:
        if group[1].find(item) != -1 and group[2].find(item) != -1:
            return item


def get_priority(item):
    if 65 <= ord(item) <= 90:
        return ord(item) - 38
    else:
        return (ord(item) - 97) + 1


total_priority = 0


groups = create_backpacks_groups()
for group in groups:
    item = find_item(group)
    total_priority += get_priority(item)

print(total_priority)
