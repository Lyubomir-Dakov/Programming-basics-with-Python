type_1 = input().lower()
r = int(input())
c = int(input())

dict_cinema = {'premiere': 12, 'normal': 7.5, 'discount': 5}
if type_1 in dict_cinema:
    price = dict_cinema.get(type_1)
    places = r*c
    revenues = price * places
    print('%.2f' % revenues + ' ' + 'leva')
