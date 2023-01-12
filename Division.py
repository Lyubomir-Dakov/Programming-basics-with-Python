n = int(input())

div_2 = []
div_3 = []
div_4 = []

for x in range(n):
    num = int(input())
    if num % 2 == 0:
        div_2.append(num)
    if num % 3 == 0:
        div_3.append(num)
    if num % 4 == 0:
        div_4.append(num)

p1 = (len(div_2) / n)*100
p2 = (len(div_3) / n)*100
p3 = (len(div_4) / n)*100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')

