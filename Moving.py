width = int(input())
length = int(input())
height = int(input())
empty_space = width * length * height

not_full_apartment = True

while not_full_apartment:
    num_blocks = input()
    if num_blocks == 'Done':
        print(f'{empty_space} Cubic meters left.')
        not_full_apartment = False
        break
    elif int(num_blocks) > empty_space:
        print(f'No more free space! You need {int(num_blocks) - empty_space} Cubic meters more.')
        not_full_apartment = False
        break
    else:
        empty_space -= int(num_blocks)
