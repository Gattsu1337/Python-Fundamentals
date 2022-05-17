amount = float(input())
years = int(input())
method = input()
percentage = 0
factor = 0
NOK = 0
MOK = 0
BS = 0
all_years = 0
if method == "Линеен":
    percentage = 100 / years
    NOK = amount * percentage / 100
    MOK = NOK / 12
    print(f"Percentage = {percentage:.2f} / NOK = {NOK:.2f} / MOK = {MOK:.2f}")
elif method == "Константно дегресивен":
    factor = float(input())
    percentage = 100 / years * factor
    print(f"Percentage = {percentage:.2f}", end=" / ")
    for year in range(1, years + 1):
        if year == years - 1 or years:
            percentage = 50
        NOK = amount * percentage / 100
        BS = amount - NOK
        amount -= BS
        print(f"NOK = {NOK:.2f}", end=" / BS = ")
        print(f"{BS:.2f}", end="; ")
elif method == "Неравномерно дегресивен":
    for year in range(1, years + 1):
        percentage = float(input())
        NOK = amount * percentage / 100
        BS = amount - NOK
        print(f"Percentage = {percentage:.2f} /")
        print(f"NOK = {NOK:.2f} /")
        if year == years:
            print(f"{BS:.2f}")
        else:
            print(f"{BS:.2f}")
        amount -= BS
else:
    for year in range(1, years + 1):
        all_years += year
    for current_year in range(1, years + 1):
        NOK = amount * current_year / all_years
        print(f"year = {current_year}", end=" / NOK = ")
        print(f"{NOK:.2f}", end="; ")
