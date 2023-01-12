x = '4 + 6 / 5 + (4 * 9 -8) / 7 * 2'
# x = '4 + 6 / 5'
lst_1 = []
lst_2 = []
result = 0
result_2 = 0
step = 0

for num in x:
    if num != ' ':
        lst_1.append(num)

        if len(lst_1) == 3 and lst_1[1] == '+':
            if num == '(':
                lst_1[2] = 0
                x_2 = x[x.index('(') + 1: x.index(')')]
                for num_2 in x_2:
                    if num_2 != ' ':
                        lst_2.append(num_2)

                        if len(lst_2) == 3 and lst_2[1] == '+':
                            result_2 = int(lst_2[0]) + int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '-':
                            result_2 = int(lst_2[0]) - int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '*':
                            result_2 = int(lst_2[0]) * int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '/':
                            result_2 = int(lst_2[0]) / int(lst_2[2])
                            lst_2 = [result_2]

                result = int(lst_1[0]) + result_2

            else:
                result = int(lst_1[0]) + int(lst_1[2])
                lst_1 = [result]

        elif len(lst_1) == 3 and lst_1[1] == '-':
            if num == '(':
                lst_1[2] = 0
                x_2 = x[x.index('(') + 1: x.index(')')]
                for num_2 in x_2:
                    if num_2 != ' ':
                        lst_2.append(num_2)

                        if len(lst_2) == 3 and lst_2[1] == '+':
                            result_2 = int(lst_2[0]) + int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '-':
                            result_2 = int(lst_2[0]) - int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '*':
                            result_2 = int(lst_2[0]) * int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '/':
                            result_2 = int(lst_2[0]) / int(lst_2[2])
                            lst_2 = [result_2]

                result = int(lst_1[0]) - result_2
                lst_1 = [result]

            else:
                result = int(lst_1[0]) - int(lst_1[2])
                lst_1 = [result]

        elif len(lst_1) == 3 and lst_1[1] == '*':
            if num == '(':
                lst_1[2] = 0
                x_2 = x[x.index('(') + 1: x.index(')')]
                for num_2 in x_2:
                    if num_2 != ' ':
                        lst_2.append(num_2)

                        if len(lst_2) == 3 and lst_2[1] == '+':
                            result_2 = int(lst_2[0]) + int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '-':
                            result_2 = int(lst_2[0]) - int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '*':
                            result_2 = int(lst_2[0]) * int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '/':
                            result_2 = int(lst_2[0]) / int(lst_2[2])
                            lst_2 = [result_2]

                result = int(lst_1[0]) * result_2
                lst_1 = [result]

            else:
                result = int(lst_1[0]) * int(lst_1[2])
                lst_1 = [result]

        elif len(lst_1) == 3 and lst_1[1] == '/':
            if num == '(':
                lst_1[2] = 0
                x_2 = x[x.index('(') + 1: x.index(')')]
                for num_2 in x_2:
                    if num_2 != ' ':
                        lst_2.append(num_2)

                        if len(lst_2) == 3 and lst_2[1] == '+':
                            result_2 = int(lst_2[0]) + int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '-':
                            result_2 = int(lst_2[0]) - int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '*':
                            result_2 = int(lst_2[0]) * int(lst_2[2])
                            lst_2 = [result_2]

                        elif len(lst_2) == 3 and lst_2[1] == '/':
                            result_2 = int(lst_2[0]) / int(lst_2[2])
                            lst_2 = [result_2]

                result = int(lst_1[0]) / result_2
                lst_1 = [result]

            else:
                result = int(lst_1[0]) / int(lst_1[2])
                lst_1 = [result]

print(result)
