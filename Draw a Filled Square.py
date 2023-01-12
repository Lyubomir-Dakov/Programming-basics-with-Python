n = int(input())


def first_and_last_line(n):
    print('-'*2*n)


def mid_square(n):
    for x in range(n-2):
        print('-' + '\\/'*int((2*n - 2)/2) + '-')



first_and_last_line(n)
mid_square(n)
first_and_last_line(n)


