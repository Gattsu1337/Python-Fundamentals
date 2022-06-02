def sorting(current_sequence):
    sorted_sequence = sorted(current_sequence)
    print(sorted_sequence)


text = input().split(' ')
numbers = list(map(int, text))
sorting(numbers)
