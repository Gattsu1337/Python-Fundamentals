first_number = int(input())
second_number = int(input())
new_list = []
for i in range(1, second_number+1):
    new_list.append(i * first_number)
print(new_list)