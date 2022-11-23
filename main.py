try:
    hour = int(input('hour->'))
    if 0 > hour :
        raise Exception('hour can not be < 0 ')
    minute = int(input('minute->'))
    if 0 > minute > 60 :
        raise Exception('minute can not be < 0 and > 60')
    second = int(input('second->'))
    if 0 > second > 60:
        raise Exception('second can not be < 0  and > 60 ')
    time = ((hour * 3600)+(minute * 60) + second)
    print('#>-<MENU>-<#')
    print('|  Kievstar |')
    print('|    Life   |')
    print('|     MTS   |')
    print('#>---------<#')
    action = input('action->')
    if action == 'Kievstar':
        kievstar = float(input('Kievstar->'))
        kiev = ((((kievstar * 100)/60) * time)/100)
        print(kiev)
    elif action == 'Life':
        life = float(input('life->'))
        lif = ((((life * 100) / 60) * time) / 100)
        print(lif)
    elif action == 'MTS':
        MTS = float(input('MTS->'))
        mts = ((((MTS * 100) / 60) * time) / 100)
        print(mts)
    else:
        print(f'Comand not found')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')