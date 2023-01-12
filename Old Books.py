book = input()
ani_is_searching = True
num_books = 0

while ani_is_searching:
    new_input = input()
    if new_input == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {num_books} books.')
        ani_is_searching = False
        break
    else:
        if new_input == book:
            print(f'You checked {num_books} books and found it.')
            ani_is_searching = False
            break
        num_books += 1