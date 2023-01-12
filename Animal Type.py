x = input()

dict_1 = {'dog':'mammal',
          'crocodile':'reptile',
          'tortoise':'reptile',
          'snake':'reptile'
          }
if x in dict_1:
    print(dict_1.get(x))
else:
    print('unknown')
