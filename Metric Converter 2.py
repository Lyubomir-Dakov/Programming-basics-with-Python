x = float(input())
metric_1 = input().lower()
metric_2 = input().lower()

if metric_1 == 'mm':
    x = x/1000
if metric_1 == 'cm':
    x = x/100
if metric_1 == 'mi':
    x = x/0.000621371192
if metric_1 == 'in':
    x = x/39.3700787
if metric_1 == 'km':
    x = x/0.001
if metric_1 == 'ft':
    x = x/3.2808399
if metric_1 == 'yd':
    x = x/1.0936133

if metric_2 == 'mm':
    x = x*1000
if metric_2 == 'cm':
    x = x*100
if metric_2 == 'mi':
    x = x*0.000621371192
if metric_2 == 'in':
    x = x*39.3700787
if metric_2 == 'km':
    x = x*0.001
if metric_2 == 'ft':
    x = x*3.2808399
if metric_2 == 'yd':
    x = x*1.0936133

print (f'{x}')