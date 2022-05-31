def even_filter(z):
    new_list = []
    for o in z:
        if o % 2 == 0:
            new_list.append(o)
    print(new_list)

sequence = map(int, input().split(' '))
even_filter(sequence)