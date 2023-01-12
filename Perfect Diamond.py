n = int(input())
num = n -1
num2 = 1
num3 = n -2
for x in range(1,n+1):
    print(' ' * num, end='')
    print('*-' * (x-1) + '*')
    num -= 1

for x in range(n-1,0,-1):
    print(' '* num2, end='')
    print('*-' *(num3) + '*')
    num3 -= 1
    num2 += 1




