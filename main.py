try:
    size = float(input('size->'))
    if 0 >= size :
        raise Exception('size can not be <= 0 ')
    speed = float(input('speed->'))
    if 0 >= speed :
        raise Exception('speed can not be <= 0  ')
    size2 = (size * 1024 * 8)
    print(size2)
    size3 = ( speed/ 1000000000)
    print(size3)
    print('#>-----------<MENU>------------<#')
    print('|  Show hour for {size} |')
    print('|  Show minute for {size}|')
    print('|  Show second for {size}|')
    print('|  other key - full time        |')
    print('#>------------------------------<#')
    action = input('action->')
    if action == 'second':
        s = (size / speed )
        print(s)
    elif action == 'minute':
        m = (size / speed/ 60 )
        print(m)
    elif action == 'hour':
        h = (size / speed / 60 / 60 )
        print(h)
    else:

        h = int(/3600)
        d = int(( % 3600) / 60)
        k = int(( % 3600) % 60)
        print(f'{h}:{d}:{k} to midnight!')