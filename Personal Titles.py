how_old = float(input())
male_fem = input()

if male_fem == 'm':
    if how_old >= 16:
        print ('Mr.')
    elif how_old < 16:
        print('Master')
elif male_fem == 'f':
    if how_old >= 16:
        print('Ms.')
    elif how_old < 16:
        print('Miss')