budget = float(input())
statisti = int(input())
obleklo_za_statist = float(input())

dekor = budget * 0.1
obleklo_costs = 0

if statisti > 150:
    obleklo_costs = statisti * obleklo_za_statist * 0.9
else:
    obleklo_costs = statisti * obleklo_za_statist

all_costs = dekor + obleklo_costs
difference = abs(budget - all_costs)

if all_costs > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')