# list_of_cards = input().split(", ")
# given_number = int(input())
#
# for iteration in range(1, given_number+1):
#     line = input().split(", ")
#     command = line[0]
#
#     if command == "Add":
#         card_name = line[1]
#         if card_name in list_of_cards:
#             print("Card is already in the deck")
#         else:
#             list_of_cards.append(card_name)
#             print("Card successfully added")
#
#     elif command == "Remove":
#         card_name = line[1]
#         if card_name in list_of_cards:
#             list_of_cards.remove(card_name)
#             print("Card successfully removed")
#         else:
#             print("Card not found")
#
#     elif command == "Remove at":
#         index = int(line[1])
#         if 0 <= index < len(list_of_cards):
#             list_of_cards.pop(index)
#             print("Card successfully removed")
#         else:
#             print("Index out of range")
#
#     else:
#         index = int(line[1])
#         card_name = line[2]
#         if 0 <= index < len(list_of_cards) and card_name not in list_of_cards:
#             list_of_cards.insert(index, card_name)
#             print("Card successfully added")
#         elif index > len(list_of_cards):
#             print("Index out of range")
#         else:
#             print("Card is already added")
#
# print(", ".join(list_of_cards))
list_of_cards = input().split(", ")
given_number = int(input())
for number in range(1, given_number+1):
    line = input().split(", ")
    command = line[0]
    if command == "Add":
        card_name = line[1]
        if card_name in list_of_cards:
            print("Card is already in the deck")
        else:
            list_of_cards.append(card_name)
            print("Card successfully added")

    elif command == "Remove":
        card_name = line[1]
        if card_name in list_of_cards:
            list_of_cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command == "Remove at":
        index = int(line[1])
        if index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif command == "Insert":
        current_index = int(line[1])
        card_name = line[2]
        if current_index < len(list_of_cards) and card_name not in list_of_cards:
            list_of_cards.insert(current_index, card_name)
            print("Card successfully added")
        elif current_index < len(list_of_cards):
            print("Index out of range")
        elif card_name in list_of_cards:
            print("Card is already added")
print(", ".join(list_of_cards))

