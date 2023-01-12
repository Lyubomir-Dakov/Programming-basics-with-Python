width = int(input())
length = int(input())

full_cake = width * length

while full_cake > 0:

    new_command = input()

    if new_command == 'STOP':
        print(f"{full_cake} pieces are left.")
        break

    taken_by_guests = int(new_command)

    if taken_by_guests > full_cake:
        diff = abs(full_cake - taken_by_guests)
        print(f"No more cake left! You need {diff} pieces more.")
        break
    else:
        full_cake -= taken_by_guests
