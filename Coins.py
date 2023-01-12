change_1 = float(input())
change = change_1 * 100
num_coins = 0


def cut_change(a):
    global change
    global num_coins
    while change >= a:
        change -= a
        num_coins += 1


def result():
    cut_change(200)
    cut_change(100)
    cut_change(50)
    cut_change(20)
    cut_change(10)
    cut_change(5)
    cut_change(2)
    cut_change(1)


result()

print(num_coins)


