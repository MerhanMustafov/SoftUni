line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")
player = ""
winner = False
if line_1[0] == line_1[1] == line_1[2]:
    winner = True
    player = line_1[0]
elif line_2[0] == line_2[1] == line_2[2]:
    winner = True
    player = line_2[0]
elif line_3[0] == line_3[1] == line_3[2]:
    winner = True
    player = line_3[0]


elif line_1[0] == line_2[0] == line_3[0]:
    winner = True
    player = line_1[0]
elif line_1[1] == line_2[1] == line_3[1]:
    winner = True
    player = line_1[1]
elif line_1[2] == line_2[2] == line_3[2]:
    winner = True
    player = line_1[2]


elif line_1[0] == line_2[1] == line_3[2]:
    winner = True
    player = line_2[1]
elif line_1[2] == line_2[1] == line_3[0]:
    winner = True
    player = line_2[1]



if winner:
    if player == "2":
        print("Second player won")
    else:
        print(f"First player won")

else:
    print(f"Draw!")