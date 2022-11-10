try:
    userseconds = int(input('input seconds->'))
    d = 24 * 3600
    if d < userseconds:
        raise Exception('All seconds per day is less then user seconds!')
    x = d - userseconds
    h = int(userseconds / 3600)
    m = int((userseconds % 3600) / 60)
    s = int((userseconds % 3600) % 60)
    print('#>---------<MENU>---------<#')
    print('|  h - Seconds in hour     |')
    print('|  m - Seconds in minutes  |')
    print('|  s - Seconds             |')
    print('|  other key - full time   |')
    print('#>------------------------<#')
    action = input('action->')
    if action == 'h':
        print(f'Hours to midnight = {int(diff_seconds/3600)} h')
    elif action == 'm':
        print(f'Minutes to midnight = {int(diff_seconds/60)} m')
    elif action == 's':
        print(f'Seconds to midnight = {diff_seconds} s')
    else:
        h = int(diff_seconds/3600)
        m = int((diff_seconds % 3600) / 60)
        s = int((diff_seconds % 3600) % 60)
        print(f'{h}:{m}:{s} to midnight!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')