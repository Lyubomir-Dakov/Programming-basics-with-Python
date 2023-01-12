n = int(input())
y= 0
z = n-4
m=1
h=1
import math
from math import ceil

if n % 2 == 0:
    #The top part
    for x in range(2,n+2,2):
        print('-' * int((n - x) / 2), end='')
        print('*',end='')
        print('-'*y,end='')
        y +=2
        print('*',end='')
        print('-' * int((n - x) / 2), end='')
        print()


    for x in range(2,n,2):
        print('-' * int(x/2), end = '')
        print('*',end='')
        print('-' * z, end = '')
        z -= 2
        print('*', end='')
        print('-' * int(x/2), end='')
        print()

else:
    for x in range(2,n+2,2):
        print('-' * math.ceil((n-x)/2), end='')
        print('*',end='')
        if x == 2:
            print('-' *0, end='')

            print('-' * math.ceil((n - x) / 2), end='')
            print()
        else:
            print('-' *m, end='')
            m += 2
            print('*', end='')
            print('-' * math.ceil((n - x) / 2), end='')
            print()

    for x in range(2,n,2):
        print('-' * h, end='')

        print('*' , end='')
        if x == n-1:
            print('-' * h, end='')
            print()
            h += 1
        else:
            print('-' * z , end = '')
            z -= 2
            print('*', end='')
            print('-' * h, end='')
            print()
            h += 1






