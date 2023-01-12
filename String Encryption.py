n = int(input())


def string_encrypt_1(symbol):
    num = ord(symbol)
    num_1 = str(num)[0]
    num_2 = str(num)[-1]
    symbol_1 = num_1 + num_2
    return symbol_1


def string_encrypt_2(symbol):
    num = ord(symbol)
    num_1 = str(num)[-1]
    num_2 = num + int(num_1)
    symbol_2 = chr(num_2)
    return symbol_2


def string_encrypt_3(symbol):
    num = ord(symbol)
    num_1 = str(num)[0]
    num_2 = num - int(num_1)
    symbol_3 = chr(num_2)
    return symbol_3


def string_part(just_symbol):
    symbol_1 = string_encrypt_1(just_symbol)
    symbol_2 = string_encrypt_2(just_symbol)
    symbol_3 = string_encrypt_3(just_symbol)
    result_for_symbol = symbol_2 + symbol_1 + symbol_3
    return result_for_symbol


for x in range(n):
    new_symbol = input()
    my_string = string_part(new_symbol)
    print(f'{my_string}', end='')
