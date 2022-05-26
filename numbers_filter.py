numb = int(input())
integer_list = []
for n in range(numb):
    integer = int(input())
    integer_list.append(integer)
filter_word = input()
filtered_list = []
for current_number in integer_list:
    if filter_word == "even":
        if current_number % 2 == 0:
            filtered_list.append(current_number)
    if filter_word == "odd":
        if current_number % 2 != 0:
            filtered_list.append(current_number)
    if filter_word == "positive":
        if current_number >= 0:
            filtered_list.append(current_number)
    if filter_word == "negative":
        if current_number < 0:
            filtered_list.append(current_number)
print(filtered_list)