import re, math

text = input()
expression = r'([\||#])(?P<item_name>[a-zA-Z ]+)(\1)(?P<exp_date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)'
total_calories = 0
result = ''
matches = re.finditer(expression, text)

for match in matches:
    total_calories += int(match.group('calories'))

    result += (f"Item: {match.group('item_name')}, Best before: {match.group('exp_date')}"
          f", Nutrition: {match.group('calories')}\n")

days = math.floor(total_calories / 2000)


print(f"You have food to last you for: {days} days!")
print(result)
