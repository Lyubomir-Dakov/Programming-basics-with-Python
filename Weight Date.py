date = input()

result = 0

y = 0
for x in date[1:]:
    y = int(date[0]) * int(x)
    result += y

u = 0
for x in date[2:]:
    u = int(date[1]) * int(x)
    result += u

i = 0
for x in date[3:]:
    i = int(date[2]) * int(x)
    result += i

o = 0
for x in date[4:]:
    o = int(date[3]) * int(x)
    result += o

p = 0
for x in date[5:]:
    p = int(date[4]) * int(x)
    result += p

a = 0
for x in date[6:]:
    a = int(date[5]) * int(x)
    result += a

s = 0
for x in date[7:]:
    s = int(date[6]) * int(x)
    result += s

print(result)

print(date)
print(len(date))
print(f'{date[:2]}-{date[2:4]}-{date[4:]}')