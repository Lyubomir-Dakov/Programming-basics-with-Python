n = int(input())

line_star = '*' * (n-2) + '\\ /' + '*' * (n-2)
line_line = '-' * (n-2) + '\\ /' + '-' * (n-2)

for x in range(1,n-1):
    if x%2 != 0:
        print(line_star)
    else:
        print(line_line)

print('@'.center(2*n-1))

line_star2 = '*' * (n-2) + '/ \\' + '*' * (n-2)
line_line2 = '-' * (n-2) + '/ \\' + '-' * (n-2)

for y in range(1,n-1):
    if y%2 != 0:
        print(line_star2)
    else:
        print(line_line2)
