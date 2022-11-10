try:
    diameter = int(input('diameter->'))
    if diameter < 0:
        raise Exception('diameter can not be < 0 !')
    print('#>---------<MENU>---------<#')
    print('|  a - area of a circle        |')
    print('|  p - perimeter of a circleм  |')
    print('#>------------------------<#')
    action = input('action->')
    import math
    r = (diameter / 2)
    if action == 'a':
        d = (math.pi * r * r )
        print (d)
    elif action == 'p':
        k = (2 * r * math.pi )
        print(k)
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
    print(f'Name: {ex.__class__.__name__}')