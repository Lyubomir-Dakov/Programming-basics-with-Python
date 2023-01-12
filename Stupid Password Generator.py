n = int(input())
l = int(input())

list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

for pass_1 in range(1, n + 1):

    for pass_2 in range(1, n + 1):

        for pass_3 in list_1[:l]:

            for pass_4 in list_1[:l]:

                for pass_5 in range(1, n + 1):
                    if pass_5 > pass_1 and pass_5 > pass_2:
                        print(f'{pass_1}{pass_2}{pass_3}{pass_4}{pass_5} ', end='')
