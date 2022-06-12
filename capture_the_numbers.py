import re
expression = r"\d+"
while True:
    text = input()
    if not text:
        break
    result = re.findall(expression, text)
    if len(result) > 0:
        print(' '.join(result), end=' ')
