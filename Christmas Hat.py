n = int(input())
# width = 4 * n +1
# height = 2 * n + 5

print('.' * int((4 * n -2)/2) + '/|\\' + '.' * int((4 * n -2)/2))
print('.' * int((4 * n -2)/2) + '\\|/' + '.' * int((4 * n -2)/2))

for x in range(2*n):
    print('.' * (int((4 * n -2)/2) - x), end='')
    print('*', end='')
    print('-'*x, end='')
    print('*', end='')
    print('-'*x, end='')
    print('*', end= '')
    print('.' * (int((4 * n -2)/2) - x), end='')
    print()

print('*' * (4 * n +1))
print('*.'* int((4 * n +1)/2) + '*')
print('*' * (4 * n +1))
