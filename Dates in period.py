from datetime import date, timedelta
start_year = int(input())
last_year = int(input())

start_date = date(start_year, 1, 1)
last_date = date(last_year, 12, 31)

delta = last_date - start_date

day = 0
for x in range(delta.days + 1):
    day = start_date + timedelta(days=x)
    date = str(day.day) + str(day.month) + str(day.year)

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
