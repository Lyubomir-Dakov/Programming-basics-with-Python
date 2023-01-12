d = int(input())
m = int(input())

dict_months = {1:31, 3:31, 5:31, 7:31, 10:31, 12: 31,
               2:28,
               4:30, 6:30, 9:30, 11:30}

new_d = d + 5
if new_d > dict_months.get(m):
    new_d -= dict_months.get(m)
    if m+1 <10:
        print(f'{new_d}.0{m + 1}')
    elif m+1 >12:
        print(f'{new_d}.01')
    else:
        print(f'{new_d}.{m+1}')

else:
    if m < 10:
        print(f'{new_d}.0{m}')
    else:
        print(f'{new_d}.{m}')



