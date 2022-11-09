metres = float(input('metres->'))
print('#>-----------------<Menu>-----------------<#')
print(f'|  mile : Show {metres} metres in miles     |')
print(f'|  inches : Show {metres} metres in inches  |')
print(f'|  yards: Show {metres} metres in yards     |')
print('#>-------------------1---------------------<#')
action = input('action->')
if action == 'mile':
    print(f'{metres} / 1609 = {metres / 1609}')
elif action == 'inches':
    print(f'{metres} * 39.37 = {metres * 39.37}')
elif action == 'yards':
    print (f'{metres} * 1.094 = {metres * 1.094}')
else:
    print('Command not found!')