number_of_wagons = int(input())
train = [0 for x in range(number_of_wagons)]
command = input()
while command != "End":
    explode = command.split(" ")
    current_command = explode[0]
    if current_command == "add":
        people = int(explode[1])
        train[-1] += people
    elif current_command == "insert":
        wagon = int(explode[1])
        people = int(explode[2])
        train[wagon] += people
    elif current_command == "leave":
        wagon = int(explode[1])
        people = int(explode[2])
        train[wagon] -= people
    command = input()
print(train)