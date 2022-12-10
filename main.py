try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    counter = 0
    for item in range(begin, end + 1):
        if item % 3 == 0 and item != 5:
            print ("«Fizz»")
    for item in range(begin, end + 1):
        if item % 5 == 0 and item != 3:
            print("«Buzz»")
    for item in range(begin, end + 1):
        if item % 5 == 0 and item % 3 == 0:
            print("Fizz Buzz")
    for item in range(begin, end + 1):
        if item % 5 != 0 and item != 3:
            print(item , end="\t")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')