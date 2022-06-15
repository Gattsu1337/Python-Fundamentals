def sum_funct(longer_word, shorter_word):
    total_sum = 0
    for i in range(len(longer_word)):
        if i < len(shorter_word):
            total_sum += ord(longer_word[i]) * ord(shorter_word[i])
        else:
            total_sum += ord(longer_word[i])

    return total_sum


def char_multiplier(first_word, second_word):
    result = 0
    if len(first_word) > len(second_word):
        result = sum_funct(first_word, second_word)
    else:
        result = sum_funct(second_word, first_word)

    print(result)


data = input().split()
char_multiplier(data[0], data[1])
