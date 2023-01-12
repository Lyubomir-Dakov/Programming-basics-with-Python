fruit = input().lower()
day = input()
quantity = float(input())

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fruits = {'banana':[2.5, 2.7],
          'apple':[1.2, 1.25],
          'orange':[0.85, 0.9],
          'grapefruit':[1.45, 1.6],
          'kiwi':[2.7, 3],
          'pineapple':[5.5, 5.6],
          'grapes':[3.85, 4.2]
          }

if fruit in fruits and day in days:
    if day in days[:-2]:
        price = fruits.get(fruit)[0]
        bill = price * quantity
        print(f'{bill:.2f}')
    elif day in days[5:]:
        price = fruits.get(fruit)[1]
        bill = price * quantity
        print(f'{bill:.2f}')
else:
    print('error')



