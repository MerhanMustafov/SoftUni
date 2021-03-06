initial_deck = input().split(":")

command = input()
new_deck = []
while not command == "Ready":
    command = command.split()

    if command[0] == 'Add':
        card_name = command[1]
        if card_name in initial_deck:
            new_deck.append(card_name)
        else:
            print("Card not found.")
    elif command[0]  == "Insert":
        card_name = command[1]
        index = int(command[2])
        if card_name in initial_deck:
            if 0 <= index < len(new_deck):
                new_deck.insert(index, card_name)
            else:
                print("Error!")
        elif not card_name in initial_deck:
            print("Error!")

    elif command[0]  == "Remove":
        card_name = command[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")

    elif command[0]  == "Swap":
        crd_1 = command[1]
        crd_2 = command[2]
        crd_1 = new_deck.index(crd_1)
        crd_2 = new_deck.index(crd_2)
        new_deck[crd_1], new_deck[crd_2] = new_deck[crd_2], new_deck[crd_1]

    elif command[0]  == "Shuffle":
        new_deck.reverse()

    command = input()
print(" ".join(new_deck))