def get_compartiments(backpack):
    middle = int(len(backpack)/2)
    return [backpack[:middle], backpack[middle:-1]]


def find_item(compartiments):
    for item in compartiments[0]:
        if compartiments[1].find(item) != -1:
            return item


def get_priority(item):
    print(item)
    if 65 <= ord(item) <= 90:
        return ord(item) - 38
    else:
        return (ord(item) - 97) + 1


total_priority = 0

with open("input.txt", "r") as data:
    for backpack in data:
        compartiments = get_compartiments(backpack)
        item = find_item(compartiments)
        print(get_priority(item))
        total_priority += get_priority(item)

print(total_priority)
