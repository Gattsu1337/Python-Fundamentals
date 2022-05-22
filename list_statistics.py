number = int(input())
positives_list = []
negatives_list = []
sum_negatives = 0
for n in range(number):
    current_number = int(input())
    if current_number < 0:
        sum_negatives += current_number
        negatives_list.append(current_number)
    else:
        positives_list.append(current_number)
print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum_negatives}")
