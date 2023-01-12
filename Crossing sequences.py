tri_a = int(input())
tri_b = int(input())
tri_c = int(input())

matrix_start = int(input())
matrix_step = int(input())

list_tri = [tri_a, tri_b, tri_c]
list_matrix = []
list_result = ['#']

x = 0
next_num = list_tri[x] + list_tri[x+1] + list_tri[x+2]

while next_num < 1000000:
    next_num = list_tri[x] + list_tri[x+1] + list_tri[x+2]
    list_tri.append(next_num)
    x += 1

y = 1


while matrix_start< 1000000:
    list_matrix.append(matrix_start)
    matrix_start += matrix_step
    if y % 2 == 0:
        matrix_step += 2
    y += 1

for z in list_tri:
    if z in list_matrix:
        print(z)
        list_result.append(z)
        break

if len(list_result) == 1:
    print('No')

# print(list_tri)
# print(list_matrix)
