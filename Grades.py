num = int(input())

top = 0
bet_4_499 = 0
bet_3_399 = 0
fail = 0
pre_average = 0

for x in range(num):
    grade = float(input())
    pre_average += grade
    if grade >= 5:
        top += 1
    elif grade >=4 and grade <=4.99:
        bet_4_499 += 1
    elif grade >= 3 and grade <= 3.99:
        bet_3_399 += 1
    else:
        fail += 1

result_top = (top / num)*100
result_bet_4_499 = (bet_4_499 / num)*100
result_bet_3_399 = (bet_3_399 / num)*100
result_fail = (fail / num)*100
average = pre_average / num

print(f"Top students: {result_top:.2f}%")
print(f"Between 4.00 and 4.99: {result_bet_4_499:.2f}%")
print(f"Between 3.00 and 3.99: {result_bet_3_399:.2f}%")
print(f"Fail: {result_fail:.2f}%")
print(f"Average: {average:.2f}")
