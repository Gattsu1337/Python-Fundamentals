def palindrome(current_numbers):
    for number in current_numbers:
        if str(number) == str(number)[::-1]:
            print(True)
        else:
            print(False)


numbers = list(map(int, input().split(', ')))
palindrome(numbers)