n = int(input())
lst = []

for x in range(n):
    y = int(input())
    lst.append(y)

print('Max number: ' + str(max(lst)))
print('Min number: ' + str(min(lst)))
