number_of_pairs = int(input())
grades_dict = {}

for current_pair in range(number_of_pairs):

    student = input()
    grade = float(input())

    if student not in grades_dict:
        grades_dict[student] = []

    grades_dict[student].append(grade)

for key, value in grades_dict.items():
    current_average = sum(value) / len(value)

    if current_average >= 4.50:
        print(f"{key} -> {current_average:.2f}")
