import string

usernames = input().split(', ')
valid = True
expected_ch = string.digits + string.ascii_letters + '_' + '-'
for nick in usernames:
    if 3 > len(nick) or len(nick) > 16 or len([x for x in nick if x in expected_ch]) != len(nick):
        valid = False
    if valid:
        print(nick)

    valid = True
