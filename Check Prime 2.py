n = int(input())

if n == 2:
    print('Prime')
else:
    x = 2
    while n > 2 and n % x !=0:
        x += 1

    if x == n:
        print('prime')
    else:
        print('Not prime')
