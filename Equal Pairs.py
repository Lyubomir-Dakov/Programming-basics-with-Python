n = int(input())

sum_pairs = 0
lst_sum = []

for i in range(1,n+1):
    x = int(input())
    y = int(input())
    sum_pairs = x+y
    lst_sum.append(sum_pairs)

z = 0
lst_minus_twins = []

if len(set(lst_sum)) == 1:
    print(f'Yes, value={sum_pairs}')
else:
    for num in lst_sum:
        while z + 1 <= len(lst_sum) - 1:
            minus_twins = abs(lst_sum[z] - lst_sum[z+1])
            z += 1
            lst_minus_twins.append(minus_twins)
    print(f'No, maxdiff={max(lst_minus_twins)}')






