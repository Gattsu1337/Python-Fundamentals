raw_key = input()
modified_key = ''
text = input()
while text != 'Generate':
    instructions = text.split(">>>")
    command = instructions[0]
    if command == 'Contains':
        substring = instructions[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        case = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        if case == 'Upper':
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
        else:
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]
        print(raw_key)
    elif command == 'Slice':
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

    text = input()

print(f"Your activation key is: {raw_key}")
