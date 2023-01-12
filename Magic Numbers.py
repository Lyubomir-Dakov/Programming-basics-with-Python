n = int(input())

for s1 in range(1,10):
    for s2 in range(1,10):
        for s3 in range(1,10):
            for s4 in range(1,10):
                for s5 in range(1,10):
                    for s6 in range(1,10):
                        if s1 * s2 * s3 * s4 * s5 * s6 == n:
                            print(f'{s1}{s2}{s3}{s4}{s5}{s6} ', end='')

