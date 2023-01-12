x = int(input())
y = int(input())

point1 = 2 <= x <= 12 and -3 <= y <= 1
point2 = 4 <= x <= 10 and -5 <= y <= 3

if point1 or point2:
    print('in')
else:
    print('out')