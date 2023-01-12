n = int(input())
m = int(input())
s = int(input())

x = m + 1
while True:
    x -= 1
    if x % 2 == 0 and x % 3 == 0:
        if x == s:
            break
        print(f'{x} ', end='')

    if x == n:
        break
