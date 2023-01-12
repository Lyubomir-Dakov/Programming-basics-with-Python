n = int(input())
num_2 = 0
num_3 = 0
num_4 = 0


for x in range(n):
    num = int(input())
    if num % 2 == 0:
        num_2 += 1

    if num % 3 == 0:
        num_3 += 1

    if num % 4 == 0:
        num_4 += 1



p1 = (num_2 / n) * 100
p2 = (num_3 / n) * 100
p3 = (num_4 / n) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')