import math
list_prime = []
list_not_prime = []


def check_prime(a):
    prime = True

    for x in range(2, int(math.sqrt(a)+1)):
        if a % x == 0:
            prime = False
            break
        elif a <= 1:
            prime = False
            break

    if prime:
        list_prime.append(a)
    else:
        list_not_prime.append(a)


while True:
    command = input()

    if command == 'stop':
        break

    num = int(command)
    if num < 0:
        print('Number is negative.')
        continue

    check_prime(num)

sum_prime = sum(list_prime)
sum_non_prime = sum(list_not_prime)

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')

