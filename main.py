try:
    start = int(input("START="))
    finish = int(input("FINISH="))
    for item in range(start , finish + 1):
        counter = 0
        for j in range(1, item + 1):
            if item % j == 0 :
                counter += 1
        if counter == 2 :
            print (item )
    print ()
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')