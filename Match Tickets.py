budget = float(input())
category = input().lower()
guests = int(input())

vip = 499.99
normal = 249.99

if category == 'vip':
    if guests in range(1,5):
        transport = budget * 0.75
        money_tickets = guests * vip
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n <0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(5,10):
        transport = budget * 0.6
        money_tickets = guests * vip
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n <0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(10,25):
        transport = budget * 0.5
        money_tickets = guests * vip
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n <0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(25,50):
        transport = budget * 0.4
        money_tickets = guests * vip
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n <0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests >= 50:
        transport = budget * 0.25
        money_tickets = guests * vip
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n <0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

if category == 'normal':
    if guests in range(1, 5):
        transport = budget * 0.75
        money_tickets = guests * normal
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n < 0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(5, 10):
        transport = budget * 0.6
        money_tickets = guests * normal
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n < 0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(10, 25):
        transport = budget * 0.5
        money_tickets = guests * normal
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n < 0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests in range(25, 50):
        transport = budget * 0.4
        money_tickets = guests * normal
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n < 0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")

    elif guests >= 50:
        transport = budget * 0.25
        money_tickets = guests * normal
        n = (budget - transport) - money_tickets
        if n >= 0:
            print(f"Yes! You have {n:.2f} leva left.")
        elif n < 0:
            print(f"Not enough money! You need {abs(n):.2f} leva.")





