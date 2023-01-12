floors = int(input())
rooms = int(input())

for x in range(floors, 0, -1):
    if x == floors:
        for y in range(rooms):
            print(f'L{x}{y} ', end='')
        print()

    else:
        if x % 2 == 0:
            for y in range(rooms):
                print(f'O{x}{y} ', end='')
            print()

        else:
            for y in range(rooms):
                print(f'A{x}{y} ', end='')
            print()

