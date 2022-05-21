first_index = int(input())
last_index = int(input())
while first_index < last_index:
    print(f"{chr(first_index)}", end=" ")
    first_index += 1
print(f"{chr(last_index)}")