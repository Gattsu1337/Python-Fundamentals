sequence = input().split()
result = ''
for item in sequence:
    result += item * len(item)
print(result)