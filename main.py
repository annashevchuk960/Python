try:
    number = int(input("number="))
    if number < 0:
        raise Exception('time can not be < 0 ')
    if 24 < number:
        raise Exception('Time can not be more than 24')
    if 0 <= number < 6:
        print("Good Night")
    elif 6 <= number < 13:
        print("Good Morning")
    elif 13 <= number < 17:
        print("Good Day")
    elif 17 <= number < 24:
        print("Good Evening")
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')