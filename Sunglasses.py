n = int(input())

for x in range(1,n+1):
    if x == 1 or x == n:
        print('*'*2*n + ' '*n + '*'*2*n)
    if x > 1 and x < n:
        if n%2 == 0 and x == n/2:
            print('*' + '/'*(2*n-2) + '*' + '|'*n + '*' + '/'*(2*n-2) + '*')
        elif n%2 != 0 and x == int(n/2 +1):
            print('*' + '/' * (2 * n - 2) + '*' + '|' * n + '*' + '/' * (2 * n - 2) + '*')
        else:
            print('*' + '/'*(2*n-2) + '*' + ' '*n + '*' + '/'*(2*n-2) + '*')
