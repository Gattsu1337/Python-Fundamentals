a = int(input())
b = int(input())
c = int(input())
highest_number = 0
if a > b and a > c:
    highest_number = a
elif b > a and b > c:
    highest_number = b
elif c > a and c > b:
    highest_number = c
print(highest_number)