x = int(input())
y = int(input())

nums_even = 0
nums_odd = 0

for num in range(x, y + 1):
    for i in str(num):
        z = 0
        while z <= len(str(num)) - 1:
            if z % 2 == 0:
                nums_odd += int(str(num)[z])
            else:
                nums_even += int(str(num)[z])
            z += 1

    if nums_even == nums_odd:
        print(f'{num} ', end='')

    nums_even = 0
    nums_odd = 0
