import math

people = int(input())
enter_tax = float(input())
bed_tax = float(input())
umbrella_tax = float(input())

num_umbrella = math.ceil(people / 2)
umbrella__full_tax = num_umbrella * umbrella_tax

num_bed = math.ceil(people * 0.75)
bed_full_tax = num_bed * bed_tax

full_enter_tax = enter_tax * people

full_costs = umbrella__full_tax + bed_full_tax + full_enter_tax

print(f"{full_costs:.2f} lv." )




