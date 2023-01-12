def triangle(num):
    z = 1
    for x in range(1, num + 1):
        for y in range(x):
            print(f'{z} ', end='')
            z += 1
        print()
        z = 1

    m = num
    for x in range(1, num):
        for y in range(m, 1, -1):
            print(f'{z} ', end='')
            z += 1
        print()
        z = 1
        m -= 1


triangle(int(input()))
