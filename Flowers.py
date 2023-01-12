num_hriz = int(input())
num_rose = int(input())
num_lale = int(input())
season = input()
holiday = input()

dict_shop = {'Spring':[2, 4.1, 2.5],
             'Summer':[2, 4.1, 2.5],
             'Autumn':[3.75, 4.5, 4.15],
             'Winter':[3.75, 4.5, 4.15]}
num_flowers = num_rose + num_hriz + num_lale
prise_hriz = num_hriz * dict_shop.get(season)[0]
prise_rose = num_rose * dict_shop.get(season)[1]
prise_lale = num_lale * dict_shop.get(season)[2]

price_buket = prise_hriz + prise_rose + prise_lale

if holiday == 'Y':
    price_buket *= 1.15
    if num_lale > 7 and season == 'Spring':
        price_buket *= 0.95
    if num_rose >= 10 and season == 'Winter':
        price_buket *=0.9
    if num_flowers > 20:
        price_buket *=0.8

else:
    if num_lale > 7 and season == 'Spring':
        price_buket *= 0.95
    if num_rose >= 10 and season == 'Winter':
        price_buket *=0.9
    if num_flowers > 20:
        price_buket *=0.8

print(f'{price_buket + 2:.2f}')



