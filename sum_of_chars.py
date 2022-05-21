lines = int(input())
total_sum = 0
for i in range(lines):
    letters = input()
    total_sum += ord(letters)
print(f"The sum equals: {total_sum}")