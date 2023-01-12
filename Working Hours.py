x = int(input())
y = input()

list_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

if x in range(10,19) and y in list_week:
    print('open')
else:
    print('closed')
