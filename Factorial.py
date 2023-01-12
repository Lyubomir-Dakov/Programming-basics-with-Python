n = int(input())
# result = n * (n-1) * ( n-2) ...... 2 * 1
x = 1
while True:
    x = x * n
    n -=1
    if not n > 1:
        break
print(x)





