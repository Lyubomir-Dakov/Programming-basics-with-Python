a = int(input())
b = int(input())

for x in range(a,b-2):
    for y in range(a+1,b-1):
        for z in range(a+2,b):
            for n in range(a+3,b+1):
                if x<y<z<n:
                    print(f'{x} {y} {z} {n}')

if b-a <3:
    print('No')


