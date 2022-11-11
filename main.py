try:
    size = float(input('size->'))
    if 0 >= size :
        raise Exception('size can not be <= 0 ')
    speed = float(input('speed->'))
    if 0 >= speed :
        raise Exception('speed can not be <= 0  ')
    size2 = (size / 125)
    gigabyte = (speed / 1000000000)
    print(gigabyte )
    print(size2)
    print('#>-----------<MENU>------------<#')
    print('|  Show hour for {size} |')
    print('|  Show minute for {size}|')
    print('|  Show second for {size}|')
    print('|  other key - full time        |')
    print('#>------------------------------<#')
    action = input('action->')
    if action == 'second':
        s = (size / gigabyte  * 1.1)
        print(s)
    elif action == 'minute':
        m = (size / gigabyte / 60  * 1.1)
        print(m)
    elif action == 'hour':
        h = (size / gigabyte / 60 / 60  * 1.1)
        print(h)
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')