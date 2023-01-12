x_first = int(input())
x_second = int(input())
x_tochka = int(input())

dif1 = abs(x_first - x_tochka)
dif2 = abs(x_second - x_tochka)

if x_tochka in range(x_first, x_second + 1) or x_tochka in range(x_second, x_first +1):
    print('in')

else:
    print('out')
print(min(dif1,dif2))
