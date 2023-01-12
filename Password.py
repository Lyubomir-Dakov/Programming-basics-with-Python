name = input()
password = input()
incorrect_password = True
while incorrect_password:
    type_pass = input()
    if type_pass == password:
        print('Welcome ' + name + '!')
        incorrect_password = False
        break
