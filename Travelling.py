ani_wats_to_travel = True

while ani_wats_to_travel:
    destination = input()

    if destination == 'End':
        ani_wats_to_travel = False
        break

    budget = float(input())
    savings = 0
    not_enough_money = True

    while not_enough_money:
        ani_saves_money = float(input())
        savings += ani_saves_money

        if savings >= budget:
            print(f"Going to {destination}!")
            not_enough_money = False
            break


