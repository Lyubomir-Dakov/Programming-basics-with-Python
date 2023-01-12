exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())
start_exam = exam_h * 60 + exam_m
arrive_exam = arrive_h * 60 + arrive_m

x = start_exam - arrive_exam

if x < 0:
    print('Late')
    if abs(x) < 60:
        print (f"{abs(x)} minutes after the start")
    elif abs(x) >=60:
        y = int(abs(x/60))
        z = abs(x) % 60
        if z <10:
            print(f"{y}:0{z} hours after the start")
        else:
            print(f"{y}:{z} hours after the start")



if x >=0 and x <=30:
    print('On time')
    if x < 60:
        print(f'{x} minutes before the start')
    elif x >= 60:
        y = int(x / 60)
        z = x % 60
        if z < 10:
            print(f"{y}:0{z} hours before the start")
        else:
            print(f"{y}:{z} hours before the start")




if x > 30:
    print('Early')
    if x < 60:
        print(f'{x} minutes before the start')
    elif x >= 60:
        y = int(x / 60)
        z = x % 60
        if z < 10:
            print(f"{y}:0{z} hours before the start")
        else:
            print(f"{y}:{z} hours before the start")


