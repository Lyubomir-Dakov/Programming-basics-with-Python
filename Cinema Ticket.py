n = input()

dict_week = {'Monday': 12,
             'Tuesday': 12,
             'Wednesday': 14,
             'Thursday': 14,
             'Friday': 12,
             'Saturday': 16,
             'Sunday': 16}

if n in dict_week:
    print(dict_week.get(n))



