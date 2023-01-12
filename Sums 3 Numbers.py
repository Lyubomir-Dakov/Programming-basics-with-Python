x = int(input())
y = int(input())
z = int(input())


if x == y + z:
    print(f'{min(y,z)} + {max(y,z)} = {x}')
elif y == x + z:
    print(f'{min(x, z)} + {max(x, z)} = {y}')
elif z == x + y:
    print(f'{min(y, x)} + {max(y, x)} = {z}')
else:
    print('No')