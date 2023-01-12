city = input().lower()
s = float(input())

dict_1 = {'sofia':[0.05, 0.07, 0.08, 0.12],
          'varna':[0.045, 0.075, 0.1, 0.13],
          'plovdiv':[0.055, 0.08, 0.12, 0.145]}

if city in dict_1:
    if s>=0 and s<=500:
        commision = s * dict_1.get(city)[0]
        print('%.2f' %commision)
    elif s>500 and s<=1000:
        commision = s * dict_1.get(city)[1]
        print('%.2f' %commision)
    elif s>1000 and s<=10000:
        commision = s * dict_1.get(city)[2]
        print('%.2f' %commision)
    elif s>10000:
        commision = s * dict_1.get(city)[3]
        print('%.2f' %commision)

if city not in dict_1 or s<0:
    print('error')



