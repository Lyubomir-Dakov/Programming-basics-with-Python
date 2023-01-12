budget = float(input())
season = input().lower()

dict_1 = {
    'bulgaria':{'summer':'Camp','winter':'Hotel'},
    'balkans':{'summer':'Camp','winter':'Hotel'},
    'europe':{'summer':'Hotel','winter':'Hotel'}
          }


if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        x = budget * 0.3
        print(f"{dict_1.get('bulgaria').get('summer')} - {x:.2f}")
    elif season == 'winter':
        x = budget * 0.7
        print (f"{dict_1.get('bulgaria').get('winter')} - {'%.2f' % x}")

elif budget >100 and budget <=1000:
    print ('Somewhere in Balkans')
    if season == 'summer':
        x = budget * 0.4
        print(f"{dict_1.get('balkans').get('summer')} - {'%.2f' % x}")
    elif season == 'winter':
        x = budget * 0.8
        print (f"{dict_1.get('balkans').get('winter')} - {'%.2f' % x}")

elif budget > 1000:
    print('Somewhere in Europe')
    if season == 'summer':
        x = budget * 0.9
        print(f"{dict_1.get('europe').get('summer')} - {'%.2f' % x}")
    elif season == 'winter':
        x = budget * 0.9
        print (f"{dict_1.get('europe').get('winter')} - {'%.2f' % x}")





