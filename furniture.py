import re
text = input()
expression = r'^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)'
total = 0
bought_furniture = []
while text != 'Purchase':
    matches = re.finditer(expression, text)
    for match in matches:
        furniture = match.group('furniture')
        price = match.group('price')
        quantity = match.group('quantity')
        total += float(price) * int(quantity)
        bought_furniture.append(furniture)

    text = input()

print(f'Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total:.2f}')