given_number = int(input())
dict_syn = {}
for current_iteration in range(given_number):
    word = input()
    synonym = input()

    if word not in dict_syn:
        dict_syn[word] = []

    dict_syn[word].append(synonym)

for word in dict_syn.keys():
    print(f"{word} - {', '.join(dict_syn[word])}")