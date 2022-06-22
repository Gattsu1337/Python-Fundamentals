player_friends = input().split(", ")
blacklisted_number = 0
lost_number = 0

line = input()
while line != "Report":
    line = line.split(" ")
    command = line[0]

    if command == "Blacklist":
        name = line[1]
        if name in player_friends:
            index = player_friends.index(name)
            player_friends[index] = "Blacklisted"
            blacklisted_number += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif command == "Error":
        index = int(line[1])
        current_name = player_friends[index]
        if 0 <= index < len(player_friends) and current_name not in ["Blacklisted", "Lost"]:
            player_friends[index] = "Lost"
            lost_number += 1
            print(f"{current_name} was lost due to an error.")

    elif command == "Change":
        index = int(line[1])
        new_name = line[2]
        if 0 <= index < len(player_friends):
            current_name = player_friends[index]
            print(f"{current_name} changed his username to {new_name}.")
            player_friends[index] = new_name

    line = input()

print(f"Blacklisted names: {blacklisted_number}")
print(f"Lost names: {lost_number}")
print(" ".join(player_friends))
