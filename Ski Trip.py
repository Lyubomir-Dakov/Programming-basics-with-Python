days = int(input())
type_room = input()
result = input()

dict_trip = {'room for one person': [18,0,0,0],
             'apartment': [25, 0.3, 0.35, 0.5],
             'president apartment': [35, 0.1, 0.15, 0.2]}

nights = days -1
costs_before_discount = nights * dict_trip.get(type_room)[0]
discount= 0


if days < 10:
    discount = costs_before_discount * dict_trip.get(type_room)[1]

elif days in range(10,16):
    discount = costs_before_discount * dict_trip.get(type_room)[2]

else:
    discount = costs_before_discount * dict_trip.get(type_room)[3]

all_costs = costs_before_discount - discount

if result == 'positive':
    all_costs *= 1.25
elif result == 'negative':
    all_costs *= 0.9

print(f'{all_costs:.2f}')






