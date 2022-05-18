from sys import maxsize
divisor = int(input())
boundary = int(input())
largest_number = -maxsize
for i in range(1, boundary+1):
    if i % divisor == 0 and 0 < i <= boundary:
        largest_number = i
print(largest_number)