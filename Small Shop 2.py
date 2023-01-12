product = input()
city = input()
quantity = float(input())

dictionary_shop = {'Sofia': {'coffee': 0.5, 'water': 0.8, 'beer': 1.2, 'sweets': 1.45, 'peanuts': 1.6},
                   'Plovdiv': {'coffee': 0.4, 'water': 0.7, 'beer': 1.15, 'sweets': 1.30, 'peanuts': 1.5},
                   'Varna': {'coffee': 0.45, 'water': 0.7, 'beer': 1.1, 'sweets': 1.35, 'peanuts': 1.55}
                   }

# Създаваме dictionary, където папълваме данните от условието
# със .get(city - например Sofia) показваме, че ще взимаме информация от реда на 'Sofia' в dictionary-то по горе
# после с .get(product - например water) показваме, че искаме да вземем стойността, която отговаря за ключа 'water'
# което в този примерен случай е 0.7

result = dictionary_shop.get(city).get(product) * quantity

print(f'{result:.2f}')




