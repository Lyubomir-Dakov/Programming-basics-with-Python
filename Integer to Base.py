def integer_to_base(number, to_base):
    result = ""
    while number != 0:
        reminder = number % to_base
        result = str(reminder) + result
        number = number // to_base
    print(result)


integer_to_base(int(input()), int(input()))



