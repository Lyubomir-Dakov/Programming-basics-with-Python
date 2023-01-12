n = int(input())
max_num = -1000000000000000000000
for num in range(n):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
print(max_num)