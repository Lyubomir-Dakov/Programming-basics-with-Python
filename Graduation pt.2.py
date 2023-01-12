name = input()
list_score = []
is_studying = True
grade = 0
bad_boy = 0

while is_studying:
    score = float(input())

    if score < 4:
        bad_boy += 1
        list_score.append(score)
        if bad_boy >= 2:
            print(f'{name} has been excluded at {grade +1} grade')
            is_studying = False
            break
    else:
        list_score.append(score)
        grade += 1
    if grade == 12:
        print(f'{name} graduated. Average grade: {sum(list_score)/12 :.2f}')
        is_studying = False

