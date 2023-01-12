flower = input()
num_flower = int(input())
budget = int(input())

roses = 5
dahlias = 3.8
tulips = 2.8
narcissus = 3
gladiolus = 2.5

costs = 0

if flower == 'Roses':
    costs = roses * num_flower
    if num_flower > 80:
        costs *= 0.9
if flower == 'Dahlias':
    costs = dahlias * num_flower
    if num_flower > 90:
        costs *= 0.85
if flower == 'Tulips':
    costs = tulips * num_flower
    if num_flower > 80:
        costs *= 0.85
if flower == 'Narcissus':
    costs = narcissus * num_flower
    if num_flower < 120:
        costs *= 1.15
if flower == 'Gladiolus':
    costs = gladiolus * num_flower
    if num_flower < 80:
        costs *=1.2


dif = abs(budget - costs)
if costs <= budget:
    print(f'Hey, you have a great garden with {num_flower} {flower} and {dif:.2f} leva left.')
else:
    print(f'Not enough money, you need {dif:.2f} leva more.')

