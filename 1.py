from math import floor

daily_biscuits_worker = int(input())
workers_count = int(input())
competition_biscuits = int(input())
monthly_biscuits = 0

for day in range(1, 31):
    if day % 3 != 0:
        monthly_biscuits += floor(daily_biscuits_worker * workers_count)
    else:
        monthly_biscuits += floor(daily_biscuits_worker * workers_count * 0.75)

print(f"You have produced {monthly_biscuits:.0f} biscuits for the past month.")

difference = abs(monthly_biscuits - competition_biscuits)
percentage = difference / competition_biscuits * 100

if competition_biscuits > monthly_biscuits:
    print(f"You produce {percentage:.2f} percent less biscuits.")
else:
    print(f"You produce {percentage:.2f} percent more biscuits.")

