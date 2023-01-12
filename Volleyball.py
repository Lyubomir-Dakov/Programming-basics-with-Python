type_year = input().lower()    # leap / normal
p = int(input())               # holidays not sat/sun
h = int(input())               # how many times in the year he travels to his city

weekends = 48
play_holidays = p * (2/3)                  #  !
play_weekends_travel = h                     # !
weekends_sofia = weekends - h
play_weekends_sofia = weekends_sofia *(3/4)   # !

if type_year == 'normal':
    result = play_holidays + play_weekends_travel + play_weekends_sofia
    print(int(result))
elif type_year == 'leap':
    result1 = play_holidays + play_weekends_travel + play_weekends_sofia
    result2 = result1 + result1 * 0.15
    print(int(result2))






