n = int(input())

line_1 = '.' * (n+1) + '_' * (2*n+1) + '.' * (n+1)
print(line_1)

y = 0
m = 0
for x in range(n+1):
    line_2 = '.' * (n-x) + '//' + '_' * (2*n - 1 +y) + '\\\\' + '.' * (n-x)
    y += 2
    if x == n:
        print('//' + '_' * int(((2*n - 1 +y)-5)/2-1) + 'STOP!' + '_' * int(((2*n - 1 +y)-5)/2-1) + '\\\\')
    else:
        print(line_2)

for z in range(n):
    line_3 = '.' * z + '\\\\' + '_' * (4*n-1-m) + '//' + '.' * z
    m+= 2
    print(line_3)

