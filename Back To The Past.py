x = float(input())
year = int(input())

years_to_live = year - 1800
list_costs_2 = []
list_costs_1 = []


for i in range(years_to_live+1):
    if i % 2 == 0:
        list_costs_2.append(12000)
    else:
        y = 12000 + 50*(18+i)
        list_costs_1.append(y)

money_needed = sum(list_costs_1) + sum(list_costs_2)
money_left = x - money_needed

if money_needed <= x:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive.")


