import math
money = float(input())
width = float(input())
lenght = float(input())
a = float(input())
h = float(input())
p_tile = float(input())
p_worker = float(input())

area_ground = width * lenght
area_tile = (a*h)/2
num_tile = math.ceil(area_ground / area_tile) + 5
p_all_tiles = num_tile * p_tile
all_costs = p_all_tiles + p_worker

dif_money = abs(all_costs - money)

if all_costs <= money:
    print(f"{dif_money:.2f} lv left.")
else:
    print(f"You'll need {dif_money:.2f} lv more.")



