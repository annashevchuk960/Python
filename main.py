try:
    number = 0
    sum = 0
    min = 0
    max = 0
    trigger = True
    while True:
        number = int(input('number->'))
        if number == 7:
            break
        else:
            sum += number
            if trigger:
                min = max = number
                trigger = False
            else:
                if max < number:
                    max = number
                if min > number:
                    min = number
    print (f'Sum = {sum}')
    print (f'Min = {min}')
    print (f'Max = {max}')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')