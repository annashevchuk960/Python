try:
    number1 = int(input("number 1="))
    number2 = int(input("number 2="))
    if  number1 == number2:
        print("Number is equal")
    elif number1 > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')