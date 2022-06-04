numbers = list(map(int, input().split(', ')))
positives_list = [str(x) for x in numbers if x >= 0]
negatives_list = [str(x) for x in numbers if x < 0]
evens_list = [str(x) for x in numbers if x % 2 == 0]
odds_list = [str(x) for x in numbers if x % 2 != 0]
print(f'Positive: {", ".join(positives_list)}')
print(f'Negative: {", ".join(negatives_list)}')
print(f'Even: {", ".join(evens_list)}')
print(f'Odd: {", ".join(odds_list)}')