num_start = int(input())
num_end = int(input())

dict_weight = {'a': 5, 'b': -12, 'c': 47, 'd': 7, 'e': -32}
list1= dict_weight.keys()
we_have_result = False

for x in list1:
    for y in list1:
        for z in list1:
            for m in list1:
                for n in list1:
                    result_1 = x + y + z + m + n
                    result_2 = []
                    for w in result_1:
                        if w not in result_2:
                            result_2.append(w)

                    list_weight = []
                    q = 1
                    for num in result_2:

                        weight_num = dict_weight.get(num) * q
                        list_weight.append(weight_num)
                        q += 1
                    weight_result_1 = sum(list_weight)
                    if weight_result_1 in range(num_start, num_end + 1):
                        print(f'{result_1} ', end='')
                        we_have_result = True

if not we_have_result:
    print('No')



