try:
    manager1 = int(input('summafirstmanager->'))
    manager2 = int(input('summasecondmanager->'))
    manager3 = int(input('summathirdmanager->'))
    print('#>-----<MENU>------<#')
    print('|    manager1  |')
    print('|     manager2   |')
    print('|    manager3    |')
    print('|   best manager |')
    print('#>------------------<#')
    action = input('->')
    if action == 'manager1':
        if manager1 <= 500:
            total1 = (200+(200 * 3 / 100))
        elif 500 < manager1 > 1000:
            total1 = (200+(200 * 5 / 100))
        elif manager1 > 1000:
            total1 = (200+(200 * 8 / 100))
        print(total1)
    elif action == 'manager2':
        if manager2 <= 500:
            total2 = (200+(200 * 3 / 100))
        elif 500 < manager2 > 1000:
            total2 = (200+(200 * 5 / 100))
        elif manager2 > 1000:
            total2 = (200+(200 * 8 / 100))
        print(total2)
    elif action == 'manager3':
        if manager3 <= 500:
            total3 = (200 +(200 * 3 / 100))
        elif 500 < manager3 > 1000:
            total3 = (200 +(200 * 5 / 100))
        elif manager3 > 1000:
            total3 = (200 +(200 * 8 / 100))
        print(total3)
    elif action == 'best manager':
        if manager2 < manager1 > manager3 :
         a=((200 +(200 * 8 / 100)) + 200)
         print('manager 3 ',a)
        elif manager1 < manager2 > manager3 :
         b = ((200 +(200 * 8 / 100)) + 200)
         print('manager 3 ',b)
        elif manager2 < manager3 > manager1 :
         c = ((200 +(200 * 8 / 100)) + 200)
         print('manager 3 ',c)
    else:
        print(f'Comand not found')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
