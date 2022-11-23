try:
    number = int(input('number->'))
    if 0 >= number :
        raise Exception('number can not be <= 0 ')
    print('#>-----<MENU>------<#')
    print('|  Show degree0 |')
    print('|  Show degree1 |')
    print('|  Show degree2 |')
    print('|  Show degree3 |')
    print('|  Show degree4 |')
    print('|  Show degree5 |')
    print('|  Show degree6 |')
    print('|  Show degree7 |')
    print('#>------------------<#')
    action = input('action->')
    if action == 'degree1':
        degree1=number
        print(degree1)
    elif action == 'degree0':
        degree0= (1)
        print(1)
    elif action == 'degree2':
        degree2= (number * number)
        print(degree2)
    elif action == 'degree3':
        degree3= (number * number * number)
        print(degree3)
    elif action == 'degree4':
        degree4= (number * number * number * number)
        print(degree4)
    elif action == 'degree5':
        degree5= (number * number * number * number * number)
        print(degree5)
    elif action == 'degree6':
        degree6= (number * number * number * number * number * number)
        print(degree6)
    elif action == 'degree7':
        degree7= (number * number * number * number * number* number * number)
        print(degree7)
    else:
        print(f'Comand not found')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')