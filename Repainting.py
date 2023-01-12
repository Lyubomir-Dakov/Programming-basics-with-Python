nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())

nylon_costs = nylon * 1.5
paint_costs = paint * 14.5
thinner_costs = thinner * 5

nylon_costs += 2 * 1.5
paint_costs *= 1.1
envelop = 0.4

costs_per_hour = 0.3 * (nylon_costs + paint_costs+ thinner_costs + envelop)
work_costs = costs_per_hour * working_hours

full_costs = nylon_costs + paint_costs + thinner_costs + envelop + work_costs

print(f"Total expenses: {full_costs:.2f} lv.")