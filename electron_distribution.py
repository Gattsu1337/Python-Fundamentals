number_of_electrons = int(input())
counter = 1
filled_shells = []
while True:
    element = 2 * (counter ** 2)
    if element < number_of_electrons:
        number_of_electrons -= element
        filled_shells.append(element)
    else:
        filled_shells.append(number_of_electrons)
        break
    counter += 1

print(filled_shells)