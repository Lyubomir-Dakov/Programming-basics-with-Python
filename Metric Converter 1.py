
x = float(input())
measure_1 = input().lower()
measure_2 = input().lower()

ddd = {'mm' : 1000 , 'cm':100,'mi' : 0.000621371192 , 'in' : 39.3700787 , 'km' : 0.001 , 'ft' : 3.2808399 , 'yd' : 1.0936133}
if measure_1 in ddd and measure_2 in ddd:
    y= float(ddd.get(measure_1))
    z= float(ddd.get(measure_2))
    result = (z/y)*x
    print(result)