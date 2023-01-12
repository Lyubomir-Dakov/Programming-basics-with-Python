numbers = True
list_num = []

while numbers:
    num = input()
    if num == 'Stop':
        numbers = False
        break
    else:
        list_num.append(int(num))

print(max(list_num))
