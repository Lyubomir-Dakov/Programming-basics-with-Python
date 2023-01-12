# Write a Python function that prints out the first
# n rows of Pascal's triangle


def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(n):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]
    return n >= 1


pascal_triangle(int(input()))
