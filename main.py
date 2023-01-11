try:
    start = int(input("START="))
    finish = int(input("FINISH="))
    for item in range(start , finish):
        for j in range(2, item):
            if item % j == 0 and item != 0:
                print(item )
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')