text = input().split()
even_list = [x for x in text if len(x) % 2 == 0]
for item in even_list:
    print(item)