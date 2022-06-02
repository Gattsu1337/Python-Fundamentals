vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
whatever = (x for x in text if x not in vowels)
print("".join(whatever))