list_of_int = input().split(" ")
copy_list = list(map(int, list_of_int))
numbers_to_remove = int(input())
for n in range(numbers_to_remove):
    min_number = min(copy_list)
    list_of_int.remove(str(min_number))
    copy_list.remove(min_number)
print(", ".join(list_of_int))
