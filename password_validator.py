def validator(current_password):
    invalid = False
    if not 6 <= len(current_password) <= 10:
        print("Password must be between 6 and 10 characters")
        invalid = True

    if not current_password.isalnum():
        print("Password must consist only of letters and digits")
        invalid = True

    if len([x for x in current_password if x.isdigit()]) < 2:
        print("Password must have at least 2 digits")
        invalid = True

    if not invalid:
        print("Password is valid")


password = input()
validator(password)