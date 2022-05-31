def even_odd(a):
    sum_odd = 0
    sum_even = 0
    for i in a:
        if i % 2 == 0:
            sum_even += i
        elif i % 2 != 0:
            sum_odd += i
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


number = map(int, list(input()))
even_odd(number)