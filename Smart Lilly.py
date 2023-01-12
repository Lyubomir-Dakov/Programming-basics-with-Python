n = int(input())
machine = float(input())
p = int(input())

gift_2 = 0
gift_1 = 0
list_gif_2 =[]

for x in range(1,n+1):
    if x % 2 == 0:
        gift_2 += 10
        list_gif_2.append(gift_2)
    else:
        gift_1 += 1

money_gift_1 = gift_1 * p
money_gift_2 = sum(list_gif_2) - len(list_gif_2)
all_money = money_gift_2 + money_gift_1
dif_money = all_money - machine

if all_money >= machine:
    print(f'Yes! {dif_money:.2f}')
else:
    print(f'No! {abs(dif_money):.2f}')








