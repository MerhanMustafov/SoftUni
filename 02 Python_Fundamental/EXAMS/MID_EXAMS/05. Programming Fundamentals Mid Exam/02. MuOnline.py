dungeons_rooms = input().split('|')
initial_health = 100
initial_bitcoins = 0
room_num = 0

for room in dungeons_rooms:
    command, number = room.split(" ")
    number = int(number)
    room_num += 1
    if command == "potion":
        if 100 - initial_health < number:
            healed_num = (100 - initial_health)
            initial_health += (100 - initial_health)
            print(f"You healed for {healed_num} hp.")
        else:
            print(f"You healed for {number} hp.")
            initial_health += number
        print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_health -= number
        if not initial_health <= 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}." )
            print(f"Best room: {room_num}")
            exit(0)

print(f"You've made it!")
print(f"Bitcoins: {initial_bitcoins}")
print(f"Health: {initial_health}")