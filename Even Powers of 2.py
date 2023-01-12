n = int(input())
x = 1
list_1 =[x]
for y in range(1,n+1):
    x = x*2
    if y % 2 == 0:
        list_1.append(x)

for z in list_1:
    print(z)



