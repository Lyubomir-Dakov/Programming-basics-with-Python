n = int(input())
salary = int(input())

dict_salary = {'Facebook': 150,
               'Instagram': 100,
               'Reddit': 50}

for x in range(n):
    opened_website = input()
    if opened_website in dict_salary:
        salary -= dict_salary.get(opened_website)
    if salary <= 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(salary)