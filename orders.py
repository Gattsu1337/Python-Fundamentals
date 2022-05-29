def calculator(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00
current_product = input()
current_quantity = int(input())
print(f"{calculator(current_product, current_quantity):.2f}")