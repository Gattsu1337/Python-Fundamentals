def sum_numbers(a, b):
    return a + b


def subtraction(current_sum, c):
     return current_sum - c


a, b, c = int(input()), int(input()), int(input())

print(subtraction(sum_numbers(a, b), c))