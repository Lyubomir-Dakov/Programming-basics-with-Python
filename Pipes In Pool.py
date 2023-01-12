v_pool = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
h_time = float(input())

all_water = (debit_p1+debit_p2)*h_time

if v_pool >= all_water:
    import math
    x =math.trunc((all_water/v_pool)*100)   # % water in the pool
    water_p1 = debit_p1 * h_time
    y =math.trunc((water_p1/all_water)*100)   # % water by pype 1
    water_p2 = debit_p2 * h_time
    z = math.trunc((water_p2/all_water)*100)   # % water by pype 2
    print(f"The pool is {x}% full. Pipe 1: {y}%. Pipe 2: {z}%.")

elif v_pool < all_water:
    x = h_time
    y = all_water - v_pool
    print(f"For {x} hours the pool overflows with {y} liters.")

