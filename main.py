try:
    userseconds = int(input('input seconds->'))
    d = 24 * 3600
    if d < userseconds:
        raise Exception('All seconds per day is less then user seconds!')
    x = d - userseconds
    h = int(userseconds / 3600)
    m = int((userseconds % 3600) / 60)
    s = int((userseconds % 3600) % 60)
    print('#>-----------<MENU>------------<#')
    print('|   Show hour for {userseconds} |')
    print('|  Show minute for {userseconds}|')
    print('|  Show second for {userseconds}|')
    print('|  other key - full time        |')
    print('#>------------------------------<#')
    action = input('action->')
    if action == 'hour':
        y = (int(x / 3600))
        print(y)
    elif action == 'minute':
        d = (int(x / 60))
        print(d)
    elif action == 'second':
        print (userseconds)
    else:
        h = int(diff_seconds/3600)
        d = int((diff_seconds % 3600) / 60)
        k = int((diff_seconds % 3600) % 60)
        print(f'{h}:{d}:{k} to midnight!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')