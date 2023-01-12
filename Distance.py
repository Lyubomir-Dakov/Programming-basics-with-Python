v_1 = int(input())          # km/h
t_1 = int(input())/60       # minutes to h
t_2 = int(input())/60       # minutes to h
t_3 = int(input())/60       # minutes to h

# s = v * t

v_2 = v_1 * 1.1
v_3 = v_2 * 0.95

s_1 = v_1 * t_1
s_2 = v_2 * t_2
s_3 = v_3 * t_3

s = s_1 + s_2 + s_3

print(f'{s:.2f}')







