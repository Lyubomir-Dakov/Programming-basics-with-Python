day_off = int(input())

work_play1 = 63
day_off_play1 = 127

day_off_full_play = day_off * day_off_play1
working_day = 365 - day_off
work_full_play = working_day * work_play1

result = work_full_play + day_off_full_play
less_more =abs(30000 - result)
h = int(less_more /60)
m = less_more % 60

if result < 30000:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")

else:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")








