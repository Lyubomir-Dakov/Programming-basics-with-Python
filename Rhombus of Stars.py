n = int(input())

for top in range(n):
    print(('* '*top).center(2*n-1))

print('* '*(n-1)+'*')

for bottom in range(n-1,0,-1):
    print (('* '*bottom).center(2*n-1))
