capacity = 255
number_of_lines = int(input())
total_liters = 0
for i in range(number_of_lines):
    current_liters = int(input())
    if current_liters <= capacity:
        capacity -= current_liters
        total_liters += current_liters
    else:
        print("Insufficient capacity!")
print(total_liters)