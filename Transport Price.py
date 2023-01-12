n = int(input())
x = input()
lst1 = ['day','night']

if x not in lst1:
    print('error')

if n < 20:
    if x =='day':
        result = n*0.79 + 0.7
        print(result)
    elif x == 'night':
        result = n*0.9 +0.7
        print(result)

if n >=20 and n<100:
    result = n*0.09
    print(result)
if n>=100:
    result = n*0.06
    print(result)


