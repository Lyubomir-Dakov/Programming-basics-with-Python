n = int(input())
left_sum = 0
right_sum = 0
for num in range(0,n):
    x = int(input())
    left_sum += x
for num in range(0,n):
    x = int(input())
    right_sum += x
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
