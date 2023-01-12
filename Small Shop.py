product = input().lower()
city = input().lower()
quantity = float(input())

sofia_dict = {'coffee':0.5,'water':0.8,'beer':1.2,'sweets':1.45,'peanuts':1.6}
plovdiv_dict = {'coffee':0.4,'water':0.7,'beer':1.15,'sweets':1.30,'peanuts':1.5}
varna_dict = {'coffee':0.45,'water':0.7,'beer':1.1,'sweets':1.35,'peanuts':1.55}

if city == 'sofia':
    if product in sofia_dict:
        price = sofia_dict.get(product)
        result = price * quantity
        print (result)

elif city == 'plovdiv':
    if product in plovdiv_dict:
        price = plovdiv_dict.get(product)
        result = price * quantity
        print (result)

if city == 'varna':
    if product in varna_dict:
        price = varna_dict.get(product)
        result = price * quantity
        print(result)



