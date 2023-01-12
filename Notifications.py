n = int(input())


def show_success_message():
    operation = input()
    message = input()
    line_1 = 'Successfully executed ' + operation + '.'
    line_2 = '=' * len(line_1)
    line_3 = message + '.'
    print(line_1)
    print(line_2)
    print(line_3)
    print('')


def show_warning_message():
    message = input()
    line_1 = 'Warning: ' + message + '.'
    line_2 = '=' * len(line_1)
    print(line_1)
    print(line_2)
    print('')


def show_error_message():
    operation = input()
    message = input()
    error_code = input()
    line_1 = 'Error: Failed to execute ' + operation + '.'
    line_2 = '=' * len(line_1)
    line_3 = 'Reason: ' + message + '.'
    line_4 = 'Error code: ' + error_code + '.'
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print('')


dict_notifications = {'success': show_success_message(),
                      'warning': show_warning_message(),
                      'error': show_error_message()}


def read_and_process_message():
    for x in range(n):
        message_type = input()
        result = dict_notifications.get(message_type)
        return result


read_and_process_message()
