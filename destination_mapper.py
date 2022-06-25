import re
places = input()
locations = []
points = 0
expression = r'([/=])([A-Z][a-zA-Z]{2,})\1'
matches = re.finditer(expression, places)
for match in matches:
    locations.append(match[2])
    points += len(match[2])
joined_locations = ', '.join(locations)
print(f"Destinations: {joined_locations}")
print(f"Travel Points: {points}")
