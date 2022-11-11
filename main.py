try:
    number = int(input("number="))
    if  number == 0:
        print("Number is equal to zero")
    elif number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')