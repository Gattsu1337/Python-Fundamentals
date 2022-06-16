def registration(current_command, parking_dict):
    current_command = current_command.split()
    command = current_command[0]
    username = current_command[1]

    if command == 'register':
        license_plate = current_command[2]
        if username not in parking_dict:
            parking_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

        elif parking_dict[username] == license_plate:
            print(f"ERROR: already registered with plate number {license_plate}")

    else:
        if username not in parking_dict:
            print(f"ERROR: user {username} not found")

        else:
            parking_dict.pop(username)
            print(f"{username} unregistered successfully")


def parking_validation():
    command_number = int(input())
    parking_dict = {}

    for current_n in range(command_number):
        user_input = input()
        registration(user_input, parking_dict)

    for user in parking_dict:
        print(f"{user} => {parking_dict[user]}")


parking_validation()
