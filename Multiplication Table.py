def multiplication_table(a, b):
    for a in range(1, 11):
        for b in range(1, 11):
            result = a * b
            print(f'{a} * {b} = {result}')


multiplication_table(1, 1)
