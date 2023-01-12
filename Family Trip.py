budget = float(input())
num_nights = int(input())
cost_per_night = float(input())
percent_additional_costs = int(input())

if num_nights > 7:
    cost_per_night *= 0.95

sleep_costs = num_nights * cost_per_night
additional_costs = budget * percent_additional_costs / 100

all_costs = sleep_costs + additional_costs

diff = abs(budget - all_costs)

if all_costs <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")