n = int(input())

# The top part of the house
if n%2==0:
    for y in range(2,n+1,2):
        print('-' * int((n - y) / 2), end='')
        print('*' * y, end='')
        print('-' * int((n - y) / 2), end='')
        print()

else:
    for y in range(1,n+1,2):
        print('-' * int((n - y) / 2), end='')
        print('*'*y,end='')
        print('-' * int((n - y) / 2), end='')
        print()

# The bottom part of the house
for x in range(1,n//2+1):
    print('|' + '*'*(n - 2) + '|')
