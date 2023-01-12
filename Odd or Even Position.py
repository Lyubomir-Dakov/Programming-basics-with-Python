n = int(input())
odd_sum = 0
odd_min = 0
odd_max = 0

even_sum = 0
even_min = 0
even_max = 0

lst_even = []
lst_odd = []

for x in range(1, n + 1):
    num = float(input())
    if x % 2 != 0:
        odd_sum += num
        lst_odd.append(num)
        odd_min = min(lst_odd)
        odd_max = max(lst_odd)

    if x % 2 == 0:
        even_sum += num
        lst_even.append(num)
        even_min = min(lst_even)
        even_max = max(lst_even)

print(f'OddSum={odd_sum:.2f},')

if len(set(lst_odd)) == 0:
    odd_max = 'No'
    odd_min = 'No'
    print(f'OddMin={odd_min},')
    print(f'OddMax={odd_max},')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if len(set(lst_even)) == 0:
    even_min = 'No'
    even_max = 'No'
    print(f'EvenMin={even_min:},')
    print(f'EvenMax={even_max:}')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')



