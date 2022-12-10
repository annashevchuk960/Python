try:
    number = 0
    trigger = True
    while True:
        number = int(input('number->'))
        if number == 7:
            print("Good bye")
            break
        else:
            if 0 < number != 7:
                print("Number is positive")
            if 0 > number:
                print("Number is negatigve")
            if number == 0:
                print("Number is equal to zero")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')