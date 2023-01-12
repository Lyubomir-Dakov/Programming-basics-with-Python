# Write a Python function that accepts a string
# and calculate the number of upper case letters
# and lower case letters.

def num_upper_lower(string):
    upper_case = 0
    lower_case = 0
    for x in string:
        if x == x.upper() and x != ' ':
            upper_case += 1
        elif x == x.lower() and x != ' ':
            lower_case += 1

    print(upper_case)
    print(lower_case)


num_upper_lower('The quick Brown Fox')
