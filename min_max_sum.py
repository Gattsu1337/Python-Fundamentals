def calculator(current_numbers):
    max_num = max(current_numbers)
    min_num = min(current_numbers)
    sum_nums = sum(current_numbers)
    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_nums}")


numbers = list(map(int, input().split(' ')))
calculator(numbers)