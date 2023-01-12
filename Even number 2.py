
while True:
    try:
        n = int(input())
        if n % 2 == 0:
            print(n)
            break
    except:
        print('Enter a valid number')