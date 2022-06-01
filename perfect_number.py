def perfect_number(current_nubmer):
    is_perfect = False
    divisors_sum = 0
    for i in range(current_nubmer-1):
        if i > 0 and current_nubmer % i == 0:
            divisors_sum += i

    if current_nubmer == divisors_sum:
        is_perfect = True

    if is_perfect:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
