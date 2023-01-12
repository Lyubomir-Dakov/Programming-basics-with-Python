n = int(input())

list_num1 = []
list_num2 = []
list_num3 = []
for x in range(1,n+1):
    num = int(input())
    if (x + 2) % 3 == 0:
        list_num1.append(num)
    if (x +1) % 3 == 0:
        list_num2.append(num)
    if x % 3 == 0:
        list_num3.append(num)

sum1 = sum(list_num1)
sum2 = sum(list_num2)
sum3 = sum(list_num3)

print(f'sum1 = {sum1}')
print(f'sum2 = {sum2}')
print(f'sum3 = {sum3}')

