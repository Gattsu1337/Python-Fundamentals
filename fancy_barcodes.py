import re
expression = r'(@#+)(?P<barcode>[A-Z][a-zA-Z0-9]+[A-Z])(@#+)'
number_of_barcodes = int(input())
for b in range(number_of_barcodes):
    text = input()
    matches = re.findall(expression, text)
    num_string = ''
    if matches:
        string = ''.join(matches[0])
        for ch in string:
            if ch.isdigit():
                num_string += ch
        if num_string:
            print(f"Product group: {num_string}")
        else:
            print(f"Product group: 00")
    else:
        print('Invalid barcode')
