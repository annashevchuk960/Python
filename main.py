try:
    size = float(input('size->'))
    if 0 >= size :
        raise Exception('size can not be <= 0 ')
    speed = float(input('speed->'))
    if 0 >= speed :
        raise Exception('speed can not be <= 0  ')
    print('#>-----------<MENU>------------<#')
    print('|  Show hour for {size} |')
    print('|  Show minute for {size}|')
    print('|  Show second for {size}|')
    print('|  other key - full time        |')
    print('#>------------------------------<#')
    action = input('action->')
    if action == 'hour':
        t = (price * gmc)
        print(t)
    elif action == 'minute':
        d = (price  * (discount / 100))
        print(d)
    elif action == 'second':
        s = ()
        print(s)
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')