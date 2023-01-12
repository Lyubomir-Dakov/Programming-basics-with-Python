n = int(input())
sum_nums = 0
max_x = -9999999999999999999999999999999999
for i in range(n):
    x = int(input())
    sum_nums += x
    if x > max_x:
        max_x = x
if sum_nums - max_x == sum_nums / 2:
    print('Yes')
    print(f'Sum = {sum_nums - max_x}')
else:
    print('No')
    print(f'Diff = {abs(sum_nums-max_x - max_x)}')
