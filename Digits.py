n = int(input())

n1 = int(str(n)[0])
n2 = int(str(n)[1])
n3 = int(str(n)[2])
broi_redove = n1 + n2
broi_chisla_na_red = n1 + n3
vsichki_chisla = broi_redove * broi_chisla_na_red
m = 0

while True:

    if n % 5 == 0:
        n = n -n1
        print(f'{n} ', end='')
        m += 1
        if m % broi_chisla_na_red == 0:
            print()
        if m == vsichki_chisla:
            break
    elif n % 3 == 0:
        n =n - n2
        print(f'{n} ', end='')
        m += 1
        if m % broi_chisla_na_red == 0:
            print()
        if m == vsichki_chisla:
            break
    else:
        n = n + n3
        print(f'{n} ', end='')
        m += 1
        if m % broi_chisla_na_red == 0:
            print()
        if m == vsichki_chisla:
            break






