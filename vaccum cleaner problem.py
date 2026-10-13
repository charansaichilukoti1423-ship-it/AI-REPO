rooms = {'A': 1, 'B': 1}
position = 'A'

while True:
    print("Vacuum cleaner is in room", position)

    if rooms[position] == 1:
        print("Room", position, "is dirty. Cleaning...")
        rooms[position] = 0
    else:
        print("Room", position, "is clean.")

    if rooms['A'] == 0 and rooms['B'] == 0:
        print("Both rooms are clean!")
        break

    if position == 'A':
        position = 'B'
    else:
        position = 'A'

print("Goal achieved!")
