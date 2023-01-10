try:
    number = int(input("length"))
    sign = (input("sign"))
    for item in range(number):
        for j in range(number):
            if item  == 0 or j == 0 or item  == number - 1 or j == number - 1:
                print(sign, end="")
            else:
                print(" ", end="")
        print("")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')