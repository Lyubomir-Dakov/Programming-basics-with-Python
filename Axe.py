n = int(input())

for x in range(n):
    line_1 = '-' * 3 * n + '*' + '-' * x + '*' + '-' * (2*n - 2 - x)
    print(line_1)

for x in range(int(n/2)):
    line_2 = '*' * (3*n+1) + '-' * (n-1) + '*' + '-' * (n -1)
    print(line_2)

if n % 2 == 0:    # all lines are 2*n
    for x in range(n - int(n/2) -1):
        line_3 = '-' * (3*n-x) + '*' + '-' * (n-1 +2*x) + '*' + '-' * (n-1 -x)
        print(line_3)
    line_4 = '-' * (2*n + int(n/2) + 1) + '*' * (2*n-1) + '-' * int(n/2)
    print(line_4)

else:    # all lines are 2*n-1
    for x in range(n - int(n/2) -2):
        line_3 = '-' * (3*n-x) + '*' + '-' * (n-1 + 2*x) + '*' + '-' * (n-1 -x)
        print(line_3)
    line_4 = '-' * (2*n + int(n/2) + 2) + '*' * (2*n-2) + '-' * (int(n/2)+1)
    print(line_4)