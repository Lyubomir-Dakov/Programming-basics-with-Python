# x = '4 + 6 / 5 + (4 * 9 -8) / 7 * 2'
# x = '4 + 6 / 5 + (4 * 9 - 8) - (4 * 9) / 7 + (1 + 2 + 4 / 5)'
x = '34 + 6 / 7'


def no_space_sequence(sequence):
    sequence_2 = ''
    for empty in sequence:
        if empty == ' ':
            continue
        else:
            sequence_2 += empty
    return sequence_2


def simple_count(short_sequence):
    lst = []
    result = 0
    for num in short_sequence:
        lst.append(num)
        if len(lst) == 3 and lst[1] == '+':
            result = int(lst[0]) + int(lst[2])
            lst = [result]
        elif len(lst) == 3 and lst[1] == '-':
            result = int(lst[0]) - int(lst[2])
            lst = [result]
        elif len(lst) == 3 and lst[1] == '*':
            result = int(lst[0]) * int(lst[2])
            lst = [result]
        elif len(lst) == 3 and lst[1] == '/':
            result = int(lst[0]) / int(lst[2])
            lst = [result]

    return result


y = no_space_sequence(x)
print(y)

z = simple_count(y)
print(z)






