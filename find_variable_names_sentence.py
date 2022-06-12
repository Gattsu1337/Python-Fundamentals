import re
text = input()
expression = r'\b_[a-zA-Z0-9]+\b'
matches = re.findall(expression, text)
word_list = []
for match in matches:
    word_list.append(match[1:])
print(','.join(word_list))