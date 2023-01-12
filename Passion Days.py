money_before_shopping = float(input())

num_stocks = 0

start_shopping = input()

while start_shopping != 'mall.Enter':
    start_shopping = input()

start_shopping = input()

while start_shopping != 'mall.Exit':

    for x in start_shopping:

        if x == '%':
            money_before_shopping *= 0.5
            num_stocks += 1

        elif x == '*':
            money_before_shopping += 10

        elif x.isupper():
            one_stock = ord(x) * 0.5
            if money_before_shopping < one_stock:
                continue
            money_before_shopping -= one_stock
            num_stocks += 1

        elif x.islower():
            one_stock = ord(x) * 0.3
            if money_before_shopping < one_stock:
                continue
            money_before_shopping -= one_stock
            num_stocks += 1

        else:
            one_stock = ord(x)
            if money_before_shopping < one_stock:
                continue
            money_before_shopping -= one_stock
            num_stocks += 1

    start_shopping = input()
    while start_shopping == 'mall.Enter':
        start_shopping = input()

if num_stocks == 0:
    print(f"No purchases. Money left: {money_before_shopping:.2f} lv.")
else:
    print(f"{num_stocks} purchases. Money left: {money_before_shopping:.2f} lv.")

