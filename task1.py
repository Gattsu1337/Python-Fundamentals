type_of_costumer = input()
total = 0
taxes = 0
while type_of_costumer != ["regular", "special"]:
    current_part = int(type_of_costumer)
    if not current_part > 0:
        print("Invalid price!")
        break
    else:
        total += current_part
        taxes += current_part * 0.2
    type_of_customer = input()
with_taxes = total * 0.8
if type_of_costumer == "special":
    with_taxes *= 0.9
if not total > 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total}$")
    print(f"Taxes: {taxes}$")
    print("-----------")
    print(f"Total price: {with_taxes}$")
