string = input().split("|")

command = input()
while not command == "Done":
    command = command.split()
    type_com = command[0]
    if type_com == "Move":
        left_right = command[1]
        index = int(command[2])
        if left_right == "Left":
            if 0 <= index - 1 <len(string):
                add = string[index]
                string.pop(index)
                string.insert(index - 1, add)
        elif left_right == "Right":
            if 0 <= index + 1 <len(string):
                add = string[index]
                string.pop(index)
                string.insert(index+1, add)
    elif type_com == "Check":
        if command[1] == "Even":
            a = [y for y in string if string.index(y) % 2 == 0]
            print(*a,sep=" ")
        elif command[1] == "Odd":
            a = [b for b in string if string.index(b) % 2 != 0]
            print(*a, sep=" ")

    command = input()
print(f"You crafted {''.join(string)}!")