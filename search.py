number = int(input())
key_word = input()
string_list = []
filtered_list = []
for i in range(number):
    current_string = input()
    string_list.append(current_string)
    if key_word in current_string:
        filtered_list.append(current_string)
print(string_list)
print(filtered_list)