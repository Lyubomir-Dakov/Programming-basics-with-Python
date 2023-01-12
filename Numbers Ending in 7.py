for num in range(1,1001):
    if len(str(num)) == 1 and num == 7:
        print(num)
    if len(str(num)) == 2 and str(num)[1] == '7':
        print(num)
    if len(str(num)) == 3 and str(num)[2] == '7':
        print (num)
