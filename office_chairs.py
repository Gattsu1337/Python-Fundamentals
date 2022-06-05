number_of_rooms = int(input())
game_on = True
free_chairs = 0
for current_room in range(number_of_rooms):
    chair_counter = 0
    info = input().split()
    chairs = info[0]
    visitors = int(info[1])
    for chair in chairs:
        if chair == "X":
            chair_counter += 1
    if chair_counter < visitors:
        print(f"{visitors - chair_counter} more chairs needed in room {current_room + 1}")
        game_on = False
    else:
        free_chairs += chair_counter - visitors

if game_on:
    print(f"Game On, {free_chairs} free chairs left")