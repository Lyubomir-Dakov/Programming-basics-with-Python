x = float(input())

if x<=10:
    print('slow')
elif x>10 and x<=50:
    print('average')
elif x>50 and x<=150:
    print('fast')
elif x>150 and x<=1000:
    print('ultra fast')
elif x>1000:
    print('extremely fast')
else:
    pass