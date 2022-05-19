number_orders = int(input())
price_per_capsule = 0
days = 0
capsules_count = 0
current_price = 0
overall_price = 0
for i in range(number_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    current_price = price_per_capsule * days * capsules_count
    overall_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")
print(f"Total: ${overall_price:.2f}")