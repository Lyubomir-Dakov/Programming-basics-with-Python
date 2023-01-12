n = int(input())
num = 1

for x in range(1,n+1):
    for y in range(1,x+1):
        print(f'{num} ', end='')
        num +=1
        if y >= x:
            print()
        if num > n:
            break
    if num > n:
        break


















