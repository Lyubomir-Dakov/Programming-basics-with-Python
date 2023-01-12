x = int(input())
w = int(input())
m = int(input())

import math
bricks_kurs_1 = w * m
kursove = math.ceil(x / bricks_kurs_1)
print(kursove)

