try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    for item in range(begin, end + 1):
        count = 0
        if (item % 5 == 0):
            count += 1
            с = ((count + item))
            print(с)
    for item in range(begin, end + 1):
        if item % 7 == 0:
            print(item, end="\t")
    for item in range(begin, end + 1):
            print(item, end="\t")
    for item in range(end, begin - 1, -1):
        print( item, end="\t")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')