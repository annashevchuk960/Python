x = float(input('x->'))
y = float(input('y->'))
z = float(input('z->'))
print('#>-----------<Menu>-----------------------<#')
print(f'|   + : Show sum for {x} and {y} and {z}   |')
print(f'|   * : Show mul for {x} and {y} and {z}   |')
print('#>----------------------------------------<#')
action = input('action->')
if action == '+':
    print(f'{x} + {y} + {z} = {x + y + z }')
elif action == '*':
    print(f'{x} * {y} * {z} = {x * y * z}')
