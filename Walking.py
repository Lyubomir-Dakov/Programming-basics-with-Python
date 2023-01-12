goal = 10000
steps_through_the_day = 0

gabi_is_walking = True

while gabi_is_walking:
    num_steps = input()


    if num_steps == 'Going home':
        num_steps = int(input())
        steps_through_the_day += int(num_steps)
        if steps_through_the_day < goal:
            diff = abs(steps_through_the_day - goal)
            print(f"{diff} more steps to reach goal.")
            gabi_is_walking = False
            break
        else:
            diff = abs(steps_through_the_day - goal)
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            gabi_is_walking = False
            break

    steps_through_the_day += int(num_steps)

    if steps_through_the_day >= goal:
        diff = abs(steps_through_the_day - goal)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        gabi_is_walking = False
        break

    # else:
    #     diff = abs(steps_through_the_day - goal)
    #     print(f"{diff} more steps to reach goal.")




