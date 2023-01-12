# S = 0.5*((x1-x2 )*(y1+y2)+(x2-x3)*(y2+y3)+(x3-x1)*(y3+y1)).

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

a = abs(x2 - x3)
h = abs(y1 - y2)
s = (a * h)/ 2
print(s)