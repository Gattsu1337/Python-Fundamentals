def rounder(whatever):
    new_list = []
    for a in whatever:
        list_a = round(float(a))
        new_list.append(list_a)
    return new_list


current_list = input().split(" ")
print(rounder(current_list))
