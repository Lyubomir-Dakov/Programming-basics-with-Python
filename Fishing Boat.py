budget = int(input())
season = input()
fisher_men = int(input())

dict_1 = {'Spring': 3000,
          'Summer': 4200,
          'Autumn': 4200,
          'Winter': 2600}

costs = dict_1.get(season)
if fisher_men <= 6:
    costs *= 0.9
elif fisher_men in range(7,12):
    costs *= 0.85
else:
    costs *= 0.75

if fisher_men % 2 == 0 and season != 'Autumn':
    costs *= 0.95

dif = abs(budget - costs)

if costs <= budget:
    print(f'Yes! You have {dif:.2f} leva left.')
else:
    print(f'Not enough money! You need {dif:.2f} leva.')