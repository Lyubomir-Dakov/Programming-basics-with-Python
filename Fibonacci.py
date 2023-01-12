n = int(input())
list_fib = [1,1]
for x in range(n):
    new_num = list_fib[x+1] + list_fib[x]
    list_fib.append(new_num)

print(list_fib[n])



