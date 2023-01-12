n = input()

list_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
if n in list_week:
    if n == list_week[5] or n == list_week[6]:
        print('Weekend')
    else:
        print('Working day')
else:
    print('Error')