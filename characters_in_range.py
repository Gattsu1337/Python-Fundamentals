def char_in_range(a, b):
    new_list = []
    for i in range(ord(a)+1, ord(b)):
        new_list.append(chr(i))
    print(" ".join(new_list))
first = input()
second = input()
char_in_range(first, second)
