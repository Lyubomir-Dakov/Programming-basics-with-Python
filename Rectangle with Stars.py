n = int(input())

print('%'*2*n)
if n % 2 == 0:    # all lines n+1
    for x in range(int((n-2)/2)):
        print('%' + ' '*(2*n -2) + '%')
else:             # all lines n+2
    for x in range(int((n-1)/2)):
        print('%' + ' '*(2*n -2) + '%')

print('%' + ' '*int((2*n-4)/2) + '*'*2 + ' '*int((2*n-4)/2) + '%')

if n % 2 == 0:    # all lines n+1
    for x in range(int((n-2)/2)):
        print('%' + ' '*(2*n -2) + '%')
else:             # all lines n+2
    for x in range(int((n-1)/2)):
        print('%' + ' '*(2*n -2) + '%')

print('%'*2*n)
