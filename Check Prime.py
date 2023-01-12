n = int(input())

import math

prime = True

for x in range(2, int(math.sqrt(n)+1)):
    if n % x == 0:
        prime = False
        break
    elif n <= 1:
        prime = False
        break


if prime:
    print('Prime')
else:
    print('Not prime')