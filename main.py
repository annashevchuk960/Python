try:
    height = int(input('height->'))
    width = int(input('width->'))
    sign = (input('sign->'))
    for item in range(0,height):
        for j in range(0, width):
            if item == 0 or item == height- 1:
                print(sign, end=" ")
            else:
                if j == 0 or j == width- 1:
                    print(sign , end=" ")
                else:
                    print(" ", end=" ")
        print()
        rectangle = (sign * height and sign * width)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')