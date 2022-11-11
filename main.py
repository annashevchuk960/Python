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
    if action == 'second':
        s = (size2 / speed )
        print(s)
    elif action == 'minute':
        m = (size2 / speed/ 60 )
        print(m)
    elif action == 'hour':
        h = (size2 / speed / 60 / 60 )
        print(h)
    else:
        s = (size2 / speed)
        h = int(s/3600)
        d = int((s % 3600) / 60)
        k = int((s % 3600) % 60)
        print(f'{h}:{d}:{k} to midnight!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')