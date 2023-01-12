total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie = input()
    student_tickets2 = 0
    standard_tickets2 =0
    kid_tickets2 = 0

    if movie == 'Finish':
        break

    sits_for_movie = int(input())
    sits = sits_for_movie

    while sits_for_movie > 0:
        type_ticket = input()

        if type_ticket == 'End':
            break

        elif type_ticket == 'student':
            student_tickets2 += 1
            student_tickets += 1
            sits_for_movie -= 1
            total_tickets += 1

        elif type_ticket == 'standard':
            standard_tickets2 += 1
            standard_tickets += 1
            sits_for_movie -= 1
            total_tickets += 1
        else:
            kid_tickets2 += 1
            kid_tickets += 1
            sits_for_movie -= 1
            total_tickets += 1

    percent_full = (student_tickets2 + standard_tickets2 + kid_tickets2) / sits * 100
    print(f"{movie} - {percent_full:.2f}% full.")

percent_student_tickets = (student_tickets / total_tickets) * 100
percent_standard_tickets = (standard_tickets / total_tickets) * 100
percent_kid_tickets = (kid_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student_tickets:.2f}% student tickets.")
print(f"{percent_standard_tickets:.2f}% standard tickets.")
print(f"{percent_kid_tickets:.2f}% kids tickets.")

