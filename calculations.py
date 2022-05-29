def calculation():
    operator = input()
    first_parameter = int(input())
    second_parameter = int(input())
    if operator == "multiply":
        result = first_parameter * second_parameter
    elif operator == "divide":
        result = first_parameter / second_parameter
    elif operator == "add":
        result = first_parameter + second_parameter
    elif operator == "subtract":
        result = first_parameter - second_parameter
    print(f"{result:.0f}")


calculation()
