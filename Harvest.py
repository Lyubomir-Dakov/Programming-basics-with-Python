# x kv m    40% for wine
# 1 kv m -> y kg grapes
# 1 l wine -> 2.5 kg grapes needed
# how much wine ?? if its enough -> separate the % between workers

x = int(input())   # area   10-5000
y = float(input()) # kg grapes in 1 kv m  0-10
z = int(input())   # l wine needed  10-600
w = int(input())   # how many workers

wine_area = x * 0.4  # kv m
all_grapes = wine_area * y  # kg
l_wine = all_grapes / 2.5  # l wine
more_or_less_wine = abs(z - l_wine)
wine_for_worker = more_or_less_wine / w

if l_wine < z:
    print(f"It will be a tough winter! More {int(more_or_less_wine)} liters wine needed.")
elif l_wine >= z:
    import math

    print(f"Good harvest this year! Total wine: {int(l_wine)} liters.")
    print(f"{math.ceil(more_or_less_wine)} liters left -> {math.ceil(wine_for_worker)} liters per person.")






