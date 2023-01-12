x = input().lower()
dict_1 = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
sum = 0
for jj in x:
    if jj in dict_1.keys():
        x = dict_1.get(jj)
        sum += x
print(sum)



