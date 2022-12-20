try:
    number = int(input('number->'))
    number1 = int(input('number1->'))
    answer = (number ** number1)
    print(answer)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
