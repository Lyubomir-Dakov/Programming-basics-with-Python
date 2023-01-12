n = int(input())
min_num = 9999999999999999999999999999
for num in range(n):
    new_num = int(input())
    if new_num < min_num:
        min_num = new_num
print(min_num)