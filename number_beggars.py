# letters_string = input().split(", ")
# letters_int = list(map(int, letters_string))
# count_beggars = int(input())
# earns = []
# for i in range(count_beggars):
#     total = [letters_int[1] for n in range(i, len(letters_int), count_beggars)]
#     money = sum(total)
#     earns.append(money)
# print(earns)
sums = input().split(", ")
sums_int = list(map(int, sums))
beggars = int(input())
earn = []

for i in range(beggars):
    total = [sums_int[i] for i in range(i, len(sums_int), beggars)]
    money = sum(total)
    earn.append(money)