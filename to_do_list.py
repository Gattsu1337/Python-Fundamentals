to_do = ["" for i in range(11)]
command = input()
while command != "End":
    explode = command.split("-")
    priority = int(explode[0])
    current_task = explode[1]
    to_do[priority] = current_task
    command = input()
final_list = [current_task for current_task in to_do if current_task != ""]
print(final_list)