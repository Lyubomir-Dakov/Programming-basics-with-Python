money = True
total = 0

while money:
    more_money = input()

    if more_money == 'NoMoreMoney':
        money = False
        break

    if float(more_money) < 0:
        print('Invalid operation!')
        money = False
        break
    else:
        print(f'Increase: {float(more_money):.2f}')
        total += float(more_money)

print(f'Total: {total:.2f}')
