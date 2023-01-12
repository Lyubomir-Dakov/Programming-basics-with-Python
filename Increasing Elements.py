n = int(input())
list_m = ['#']
list_num = [1]
num = 1

for x in range(1,n+1):
    try:
        m = int(input())
        list_m.append(m)
        if x > 1:
            if list_m[x] > list_m[x-1]:
                num += 1
                list_num.append(num)
            else:
                num = 1
    except:
        print('EOF')

if n == 0:
    print(0)
else:
    print(max(list_num))




