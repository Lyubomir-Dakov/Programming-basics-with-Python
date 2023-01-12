n = int(input())
m = int(input())

kuku = 0

for x in range(-n,n+1):
    for y in range(-n,n+1):
        for z in range(x+1,n+1):
            for a in range(y+1,n+1):
                c = abs(x-z)
                d = abs(y-a)
                s = c * d
                if c*d >= m:
                    print(f'({x}, {y}) ({z}, {a}) -> {s}')
                    kuku += 1

if kuku == 0:
    print('No')





