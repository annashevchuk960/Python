try:
    number = int(input("number "))
    for i in range(1 ,10+1):
        for j in range(1 ,10+1):
            if number == i:
                print(f'|{i} * {j} = {i * j}|')
            else:
                print(f"{i} * {j} = {i * j}")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')