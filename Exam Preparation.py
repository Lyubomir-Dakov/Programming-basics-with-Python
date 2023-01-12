bad_score = int(input())
martin_is_not_failed = True
list_task = []
list_score = []
failed_task = 0

while martin_is_not_failed:
    task = input()
    list_task.append(task)

    if task == 'Enough':
        print(f'Average score: {sum(list_score) / len(list_score):.2f}')
        print(f"Number of problems: {len(list_score)}")
        print(f"Last problem: {list_task[-2]}")
        martin_is_not_failed = False
        break

    score = int(input())
    list_score.append(score)

    if score <= 4:
        failed_task += 1

    if failed_task == bad_score:
        print(f"You need a break, {failed_task} poor grades.")
        martin_is_not_failed = False
        break
