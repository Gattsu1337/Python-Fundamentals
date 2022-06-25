import re
expression = r'([:*]{2})([A-Z][a-z]{2,})(\1)'
text = input()
cool_threshold = 1
emoji_counter = 0
list_cool = []
for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)
print(f'Cool threshold: {cool_threshold}')
matches = re.findall(expression, text)
for match in matches:
    emoji_coolness = 0
    emoji = ''.join(match)
    emoji_counter += 1
    for n in emoji:
        if n not in ['*', ':']:
            emoji_coolness += ord(n)
    if emoji_coolness >= cool_threshold:
        list_cool.append(emoji)

print(f'{emoji_counter} emojis found in the text. The cool ones are:')
for e in list_cool:
    print(e)
