hours = int(input())
minutes = int(input())

if minutes <45:
    print (f'{hours}:{minutes+15}')
elif minutes ==45:
    if hours == 23:
        print('0:00')
    else:
        print (f'{hours+1}:00')
elif minutes >45 and minutes < 55:
    if hours ==23:
        print(f'0:0{minutes+15-60}')
    else:
        print(f'{hours+1}:0{minutes+15-60}')
elif minutes >=55 and minutes <60:
    if hours ==23:
        print(f'0:{minutes+15-60}')
    else:
        print(f'{hours+1}:{minutes+15-60}')





