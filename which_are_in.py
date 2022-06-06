first = input().split(", ")
second = input().split(", ")
new_list = []

for item in first:
    for two in second:
        if item in two and item not in new_list:
            new_list.append(item)
print(new_list)
