targets = list(map(int, input().split(" ")))
command = input()
while command != "End":
    command = command.split(" ")
    word = command[0]
    index = int(command[1])
    value = int(command[2])
    if word == "Shoot" and len(targets) > index >= 0:
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target
    elif word == "Add":
        if len(targets) > index >= 0:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif word == "Strike":
        current_target = targets[index]
        if index-value < 0 or index+value >= len(targets):
            print("Strike missed!")
        else:
            targets = targets[:index-value] + targets[index+value+1:]
    command = input()
final = map(str, targets)
print("|".join(final))
