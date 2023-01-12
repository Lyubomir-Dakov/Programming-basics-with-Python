has_to_end = False
for x in range(1,4):
    if has_to_end == False:
        for y in range(3,0,-1):
            if x + y == 2:
                has_to_end = True
                break
            print(f'{x} {y}')






