budget = float(input())
season = input()

dict_journey = {'Bulgaria': {'summer': 0.3, 'winter': 0.7},
                'Balkans': {'summer': 0.4, 'winter': 0.8},
                'Europe': {'summer': 0.9, 'winter': 0.9}
                }
destination = 0
type_journey = 0

if budget <= 100:
    destination = 'Bulgaria'
elif budget <= 1000:
    destination = 'Balkans'
else:
    destination = 'Europe'

if season == 'summer' and destination != 'Europe':
    type_journey = 'Camp'
else:
    type_journey = 'Hotel'


costs = budget * dict_journey.get(destination).get(season)

print(f'Somewhere in {destination}')
print(f'{type_journey} - {costs:.2f}')
