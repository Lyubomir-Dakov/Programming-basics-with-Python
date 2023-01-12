num_stock = int(input())

mikrobus = []       # p = 200 / t
kamion = []         # p = 175 / t
vlak = []           # p = 120 / t

for x in range(num_stock):
    ton_stock = int(input())
    if ton_stock <=3:
        mikrobus.append(ton_stock)
    if ton_stock > 3 and ton_stock <= 11:
        kamion.append(ton_stock)
    if ton_stock > 11:
        vlak.append(ton_stock)

all_ton_stock = sum(mikrobus) + sum (kamion) + sum(vlak)
p1 = sum(mikrobus) / all_ton_stock
p2 = sum(kamion) / all_ton_stock
p3 = sum(vlak) / all_ton_stock

average_price_per_ton = 200*p1 + 175*p2 + 120*p3

print(f'{average_price_per_ton:.2f}')
print(f'{p1*100:.2f}%')
print(f'{p2*100:.2f}%')
print(f'{p3*100:.2f}%')

