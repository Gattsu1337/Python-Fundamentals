import re
text = input()
word = input()
counter = 0
expression = rf'\b{word}\b'
matches = re.findall(expression, text, re.IGNORECASE)
for match in matches:
    counter += 1
print(counter)