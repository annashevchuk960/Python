x = float(input('x->'))
y = float(input('y->'))
z = float(input('z->'))
print('#>-----------<Menu>-----------<#')
print(f'| min3 : between {x}, {y}, {z}      |')
print(f'| max3 : between {x}, {y}, {z}      |')
print(f'| avg3 : between {x}, {y}, {z}      |')
print('#>----------------------------<#')
action = input('action->')
if action == '+':
    print(f'{x} + {y} = {x + y}')
elif action == 'avg3':
    print(f'Avg = {(x+y+z)/3}')
elif action == 'max3':
    if x >= y and x >= z:
        print(f'Max is {x}')
    elif y >= x and y >= z:
        print(f'Max is {y}')
    elif z >= x and z >= y:
        print(f'Max is {z}')
    else:
        print(f'All values is equil!')
elif action == 'min3':
    if x <= y and x <= z:
        print(f'Min is {x}')
    elif y <= x and y <= z:
        print(f'Min is {y}')
    elif z <= x and z <= y:
        print(f'Min is {z}')
    else:
        print(f'All values is equil!')
else:
    print('Command not found!')