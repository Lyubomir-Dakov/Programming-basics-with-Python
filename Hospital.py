days = int(input())
doctors = 7
list_happy_patients = []
list_unhappy_patients = []


for i in range(1,days+1):
    patients = int(input())
    if patients > doctors:
        list_happy_patients.append(doctors)
        list_unhappy_patients.append(patients - doctors)
    if patients <= doctors:
        list_happy_patients.append(patients)
    if (i+1) % 3 == 0 and sum(list_unhappy_patients) > sum(list_happy_patients):
        doctors += 1

print(f"Treated patients: {sum(list_happy_patients)}.")
print(f"Untreated patients: {sum(list_unhappy_patients)}.")


