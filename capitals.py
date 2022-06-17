country_names = input().split(", ")
country_capitals = input().split(", ")
result = dict(zip(list(country_names), list(country_capitals)))
for key, value in result.items():
    print(f"{key} -> {value}")

