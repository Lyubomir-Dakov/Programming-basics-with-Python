hours = int(input())   # 0-200 000 need to do the project
days = int(input())    # 0-20 000 num days the firm has
workers = int(input()) # 0 -200

working_days = days * 0.9
overtime_hours = workers * working_days * 2
working_hours = workers * working_days * 8
full_hours = overtime_hours + working_hours


hours_less_or_more = int(abs(hours - full_hours))

if hours <= full_hours:
    print(f"Yes!{hours_less_or_more} hours left.")
elif hours > full_hours:
    print(f"Not enough time!{hours_less_or_more} hours needed.")


