n = int(input())

for row in range(1,n+1):
    for col in range(1,n-row+1):
        print(' ',end='')
    print('*',end='')

    for cow in range(1,row):
        print(' *',end='')
    print()


for x in range(1,n):
    for y in range(1,x):
        print(' ',end='')
    print(' *',end='')
    for y in range(1,n-x):
        print(' *',end='')
    print()


