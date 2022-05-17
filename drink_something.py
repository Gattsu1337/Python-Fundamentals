age = int(input())
beverage = ""
if age <= 14:
    beverage = "toddy"
elif 14 < age <= 18:
    beverage = "coke"
elif 18 < age <= 21:
    beverage = "beer"
elif age > 21:
    beverage = "whisky"
print(f"drink {beverage}")
