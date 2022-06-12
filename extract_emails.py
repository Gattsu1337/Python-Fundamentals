import re

text = input()
user = '( |^)[A-Za-z1-9]+((\.|\-|"\_)([A-Za-z1-9]+))*'
host = '[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
email = rf'{user}@{host}'
matches = re.finditer(email, text)
for match in matches:
    print(match[0])