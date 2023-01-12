n = int(input())

print('/', end = '')
print('^' * int(n/2), end='')
print('\\', end = '')
print('_' * (2*n - (int(n/2) + 2)*2), end='')
print('/', end = '')
print('^' * int(n/2), end='')
print('\\', end = '')
print()

for x in range(1,n-1):
    if x == n-2:
        print('|' , end= '')
        print(' ' * int(n/2+1), end= '')
        print('_' * (2*n - (int(n/2) + 2)*2), end = '')
        print(' ' * int(n/2+1), end= '')
        print('|' , end = '')
        print()

    else:
        print('|', end='')
        print(' ' * (2*n -2), end='')
        print('|', end='')
        print()

print('\\', end='')
print('_' * int(n/2), end='')
print('/', end='')
print(' ' * (2*n - (int(n/2) + 2)*2), end='')
print('\\', end='')
print('_' * int(n/2), end='')
print('/', end='')
print()



