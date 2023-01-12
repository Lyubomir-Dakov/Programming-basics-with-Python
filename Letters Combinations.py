first = input()
second = input()
third = input()

list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

index_first = list_1.index(first)
index_second = list_1.index(second)

list_2 = list_1[index_first : index_second + 1]

num_combinations = 0

for x in list_2:
    if x!= third:
        for y in list_2:
            if y != third:
                for z in list_2:
                    if z != third:
                        list_3 = x + y + z
                        print(f'{list_3} ', end='')
                        num_combinations += 1

print(num_combinations)


