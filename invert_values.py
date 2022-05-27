string = input().split(" ")
new = []
for current_num in string:
    if int(current_num) >= 0:
        new.append(-int(current_num))
    else:
        new.append(abs(int(current_num)))
print(new)
