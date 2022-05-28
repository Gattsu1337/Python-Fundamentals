received_list = input().split(" ")
absolute_list = []
for a in received_list:
    absolute_list.append(abs(float(a)))
print(absolute_list)