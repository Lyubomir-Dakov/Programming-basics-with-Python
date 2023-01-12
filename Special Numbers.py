n = int(input())

for x in range(1111,9999):
    if '0' not in str(x) and n % int(str(x)[0]) == 0 and n % int(str(x)[1]) == 0 and n % int(str(x)[2]) == 0 and n % int(str(x)[3]) == 0:
        print(f'{x} ', end='')

