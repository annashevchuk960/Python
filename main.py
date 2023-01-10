try:
    height = int(input('height->'))
    width = int(input('width->'))
    sign = (input('sign->'))
    for item in range(height ,width + 1):
        rectangle = (sign * height and sign * width)
        print  (rectangle)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')