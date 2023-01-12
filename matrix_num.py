matrix_start = int(input())
matrix_step = int(input())

list_matrix = []

for x in range(1,12):
    list_matrix.append(matrix_start)
    matrix_start += matrix_step
    if x % 2 == 0:
        matrix_step += 2



print(list_matrix)





