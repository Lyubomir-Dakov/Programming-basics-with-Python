n = int(input())


def print_line(start, end):
    for x in range(start, end + 1):
        print(f'{x} ', end='')
    print()


for x in range(n):
    print_line(1, x)

print_line(1,n)

for x in range(n-1, 0, -1):
    print_line(1,x)
    