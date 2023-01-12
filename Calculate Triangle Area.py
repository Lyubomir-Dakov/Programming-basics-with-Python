def area_triangle(a, h):
    s = (a*h)/2
    return s


a = float(input())
h = float(input())

result = area_triangle(a, h)

if result == int(result):
    print(f'{result:.0f}')
else:
    print(result)
