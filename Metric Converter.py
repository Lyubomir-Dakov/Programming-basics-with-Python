x = float(input())
y = input()
z = input()

dict_num = {'m': [1000,100], 'cm': [10, 0.01], 'mm': [0.1, 0.001]}

if y =='m' and z =='mm':
    result = x * dict_num.get('m')[0]
    print(f'{result:.3f}')
if y =='m' and z == 'cm':
    result = x * dict_num.get('m')[1]
    print(f'{result:.3f}')
if y == 'cm' and z =='mm':
    result = x * dict_num.get('cm')[0]
    print(f'{result:.3f}')
if y == 'cm' and z == 'm':
    result = x * dict_num.get('cm')[1]
    print(f'{result:.3f}')
if y == 'mm' and z =='cm':
    result = x * dict_num.get('mm')[0]
    print(f'{result:.3f}')
if y == 'mm' and z =='m':
    result = x * dict_num.get('mm')[1]
    print(f'{result:.3f}')


