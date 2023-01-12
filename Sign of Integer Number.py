

def check_num(num):
    if int(num) < 0:
        print(f'The number {num} is negative.')
    elif int(num) == 0:
        print(f'The number 0 is zero.')
    else:
        print(f'The number {num} is positive.')

check_num(input())
