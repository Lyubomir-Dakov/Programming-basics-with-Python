n = int(input())

if n%2 != 0:
    line_1 = '.' * int((n-1)/2) + '#' * n + '.' * int((n-1)/2)
    print(line_1)
    for x in range(n-2):
        line_2 = '.' * int((n-1)/2) + '#' + '.' * (n-2) + '#' + '.' * int((n-1)/2)
        print(line_2)

    line_3 = '#' * int((2*n-1 - (n-2))/2) + '.' * (n-2) + '#' * int((2*n-1 - (n-2))/2)
    print(line_3)

    z=0
    for y in range(1,n-1):
        line_4 = '.' * y + '#' + '.' * (2*n - 3 - 2*y) + '#' + '.' * y

        z += 2
        print(line_4)

    line_5 = '.' * (n-1) + '#' + '.' * (n-1)
    print(line_5)

