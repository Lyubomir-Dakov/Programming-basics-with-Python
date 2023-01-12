x = int(input())
y = int(input())

if x in range(2,13) and y in range(-3,2):
    print('in')
elif x in range(4,11) and y in range(-5,4):
    print('in')
else:
    print('out')