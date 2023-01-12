n = int(input())             # x от y в % e  (x / y)*100
list_0_199 = []
list_200_399 = []
list_400_599 = []
list_600_799 = []
list_800_1000 = []



for x in range(n):
    num = int(input())
    if num in range(0,200):
        list_0_199.append(num)
    elif num in range(200,400):
        list_200_399.append(num)
    elif num in range(400,600):
        list_400_599.append(num)
    elif num in range(600,800):
        list_600_799.append(num)
    elif num in range(800,1001):
        list_800_1000.append(num)

list_full = list_0_199 + list_200_399 + list_400_599 + list_600_799 + list_800_1000

p1 = (len(list_0_199) / len(list_full))*100
p2 = (len(list_200_399) / len(list_full))*100
p3 = (len(list_400_599) / len(list_full))*100
p4 = (len(list_600_799) / len(list_full))*100
p5 = (len(list_800_1000) / len(list_full))*100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')





