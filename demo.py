amount = float(input())
years = int(input())
method = input()
percentage = 0
factor = 0
NOK = 0
MOK = 0
BS = 0
all_years = 0
year_dict = 0
if method == "Неравномерно дегресивен":
    for year in range(1, years + 1):
        year_dict = {}
        NOK = amount * percentage / 100
        BS = amount - NOK
        print(f"Percentage = {percentage:.2f}", end=" / NOK =")
        print(f"NOK = {NOK:.2f}", end=" / BS = ")
        if year == years:
            print(f"{BS:.2f}", end="")
        else:
            print(f"{BS:.2f}", end=" / ")
        amount -= BS

