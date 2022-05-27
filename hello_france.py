items = input().split("|")
budget = int(input())
profit = 0
new_list = []
final_list = []
condition = False
for item in items:
    current_item = item.split("->")
    type_of_item = current_item[0]
    item_price = float(current_item[1])
    if type_of_item == "Clothes" and item_price <= 50:
        condition = True
    elif type_of_item == "Shoes" and item_price <= 35:
        condition = True
    elif type_of_item == "Accessories" and item_price <= 20.50:
        condition = True
    if condition:
        if budget >= item_price:
            budget -= item_price
            profit += item_price * 0.40
            new_price = item_price + (item_price * 0.40)
            new_list.append(new_price)
            final_list.append(f"{new_price:.2f}")
print(" ".join(final_list))
print(f"Profit: {profit:.2f}")
total_sum = budget + sum(new_list)
if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
