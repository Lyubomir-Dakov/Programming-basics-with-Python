money_needed = float(input())
cash = float(input())
not_enough_money = True
num_spend_money = 0
num_days = 0

while not_enough_money:
    action = input()
    spend_or_saved_money = float(input())
    num_days += 1

    if action == 'spend':
        num_spend_money += 1

        if num_spend_money == 5:
            print("You can't save the money.")
            print(f"{num_days}")
            not_enough_money = False
            break

        if spend_or_saved_money > cash:
            cash = 0
        else:
            cash -= spend_or_saved_money

    elif action == 'save':
        num_spend_money = 0
        cash += spend_or_saved_money

        if cash >= money_needed:
            print(f"You saved the money for {num_days} days.")
            not_enough_money = False
            break
