x = int(input())
y = int(input())
magic_number = int(input())
combination_number = 0
list_combination = []
list_a = []
list_b = []

for a in range(x, y+1):
    for b in range(x, y+1):
        result = a + b
        combination_number += 1
        if a + b == magic_number:
            list_combination.append(combination_number)
            list_a.append(a)
            list_b.append(b)

if len(list_combination) == 0:
    print(f"{combination_number} combinations - neither equals {magic_number}")
else:
    print(f"Combination N:{list_combination[0]} ({list_a[0]} + {list_b[0]} = {magic_number})")


