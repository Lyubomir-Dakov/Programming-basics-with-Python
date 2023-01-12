n_days = int(input())           # working days in a month
m_money = float(input())        # money per day in dollars
dollar_bgn = float(input())     # dollar to lev

money_in_bgn = m_money * dollar_bgn
month_salary = n_days * money_in_bgn      # salary in lev
year_bonus = 2.5 * month_salary

year_salary = month_salary * 12 + year_bonus
salary_after_tax = year_salary - 0.25 * year_salary

profit_per_day = salary_after_tax / 365

print('%.2f' % profit_per_day)




