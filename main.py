try:
    number = int(input('number->'))
    factorial = 1
    for item in range(1,number + 1):
        factorial *= item
        print(f'{number}! = {factorial}')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')