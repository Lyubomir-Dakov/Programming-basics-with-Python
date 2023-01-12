# n = '56788'
n = input()
x = 0
y = 0
while True:
    x = x + int(n[y])
    y += 1
    if not y < len(n) and int(n) > 0:
        break
print(x)

