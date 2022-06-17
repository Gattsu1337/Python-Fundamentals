company_dict = {}
command = input()
while command != 'End':
    info = command.split(' -> ')
    company_name = info[0]
    user_id = info[1]
    if company_name not in company_dict:
        company_dict[company_name] = []
    if user_id in company_dict[company_name]:
        pass
    else:
        company_dict[company_name].append(user_id)

    command = input()

for key, item in company_dict.items():
    print(key)
    for i in item:
        print(f"-- {i}")

