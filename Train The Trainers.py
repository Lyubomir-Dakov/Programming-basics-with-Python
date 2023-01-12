n = input()
score_all_presentations = []


while True:
    presentation = input()

    if presentation == 'Finish':
        break

    num = int(n)

    pre_average_score = 0

    for x in range(num):
        score = float(input())
        pre_average_score += score
        score_all_presentations.append(score)

    average_score = pre_average_score / num

    print(f'{presentation} - {average_score:.2f}.')

average_score_all_presentations = sum(score_all_presentations) / len(score_all_presentations)
print(f"Student's final assessment is {average_score_all_presentations:.2f}.")

