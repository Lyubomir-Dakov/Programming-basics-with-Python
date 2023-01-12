n = int(input())

hundreds_and_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
                     5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
         16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}


def short_number(number):
    if len(number) == 1:
        result = int(number)
        print(hundreds_and_ones.get(result))


def middle_number(number):
    if len(number) == 2:

        if int(number) in tens:
            print(tens.get(int(number)))

        elif int(number) in teens:
            print(teens.get(int(number)))

        else:
            num_1 = int(number[0])
            num_2 = int(number[1])
            print(f'{tens.get(num_1 * 10)}-{hundreds_and_ones.get(num_2)}')


def big_number(number):
    if len(number) == 3:

        if int(number) / 100 in hundreds_and_ones:
            print(f'{hundreds_and_ones.get(int(int(number) / 100))}-hundred')

        elif int(number[1:]) in teens:
            print(f'{hundreds_and_ones.get(int(int(number) / 100))}-hundred and {teens.get(int(number[1:]))}')

        elif int(number[1:]) in tens:
            print(f'{hundreds_and_ones.get(int(int(number) / 100))}-hundred and {tens.get(int(number[1:]))}')

        else:
            num_1 = hundreds_and_ones.get(int(int(number) / 100))
            num_2 = tens.get(int(number[1] * 10))
            num_3 = hundreds_and_ones.get(int(number[2]))
            print(f'{num_1}-hundred and {num_2} {num_3}')
            print(num_2)


big_number(input())
