courses_dict = {}
command = input()

while command != 'end':

    info = command.split(' : ')
    current_course = info[0]
    current_student = info[1]

    if current_course not in courses_dict:
        courses_dict[current_course] = []

    courses_dict[current_course].append(current_student)

    command = input()

for key, value in courses_dict.items():

    print(f"{key}: {len(value)}")

    for student in value:
        print(f"-- {student}")
