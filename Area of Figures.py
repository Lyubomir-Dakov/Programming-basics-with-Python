x = input()
if x =='square':
    y = float(input())
    s = y**2
    print('%.3f'% s)

if x == 'rectangle':
    y = float(input())
    z = float(input())
    s = y*z
    print('%.3f'% s)

if x == 'circle':
    import math
    from math import pi
    r = float(input())
    s = pi*r**2
    print('%.3f'% s)

if x == 'triangle':
    y = float(input())
    h = float(input())
    s = (y*h)/2
    print('%.3f'% s)





