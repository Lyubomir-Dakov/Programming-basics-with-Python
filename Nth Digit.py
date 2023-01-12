number = input()
index = int(input())


def find_nth_digit(number, index):
    result = number[-index]
    print(result)


find_nth_digit(number, index)