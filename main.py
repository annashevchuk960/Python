try:
    price = float(input('price->'))
    if 0 >= price :
        raise Exception('price can not be < 0 ')
    gmc = float(input('the number of game consoles->'))
    if 0 >= gmc :
        raise Exception('the number of game consoles can not be < 0 ')
    discount = float(input('discount->'))
    if 0 > discount :
        raise Exception('discount can not be < 0 ')
    print('#>-----------<Menu>-----------<#')
    print(f'| t - total amount              |')
    print(f'| d - game console at a discount |')
    print(f'| k - total amount at a discount |')
    print('#>----------------------------<#')
    action = input('action->')
    if action == 't':
        t = (price * gmc)
        print(t)
    elif action == 'd':
        d = (price  * (discount / 100))
        print(d)
    elif action == 'k':
        k = (price  * (discount / 100) * gmc )
        print(k)
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')