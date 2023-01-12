record = float(input())     # seconds
metri = float(input())       # meters
vreme_za_1m = float(input())   # seconds
import math

vreme_za_allm = vreme_za_1m * metri + math.floor(metri/15) * 12.5
dif = abs(vreme_za_allm - record)

if vreme_za_allm < record:
    print(f'Yes, he succeeded! The new world record is {vreme_za_allm:.2f} seconds.')
else:
    print(f'No, he failed! He was {dif:.2f} seconds slower.')


