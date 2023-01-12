n = int(input())


def show_success_message(operation, message):
    line_1 = 'Successfully executed ' + operation + '.'
    line_2 = len(line_1) * '='
    line_3 = message + '.'
    print(line_1)
    print(line_2)
    print(line_3)


def show_warning_message(message):
    line_1 = 'Warning: ' + message + '.'
    line_2 = len(line_1) * '='
    print(line_1)
    print(line_2)


def show_error_message(operation, message, error_code):
    line_1 = 'Error: Failed to execute ' + operation + '.'
    line_2 = len(line_1) * '='
    line_3 = 'Reason: ' + message + '.'
    line_4 = 'Error code: '+ error_code + '.'
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)


def read_and_process_message():
    for x in range(n):
        notification = input()

        if notification == 'success':
            show_success_message(input(), input())

        if notification == 'warning':
            show_warning_message(input())

        if notification == 'error':
            show_error_message(input(), input(), input())

        if x < n - 1:
            add_line = ' '
            print(add_line)


read_and_process_message()
