number = float(input())
definition = ''
extra_definition = ''
if number == 0:
    definition = 'zero'
elif number > 0:
    definition = 'positive'
else:
    definition = 'negative'
if abs(number) < 1 and number != 0:
    extra_definition = 'small'
elif abs(number) > 1000000:
    extra_definition = 'large'
print(f"{extra_definition} {definition}")