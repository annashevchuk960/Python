try:
    begin = int(input('begin->'))
    end = int(input('end->'))
    sum = 0
    sum1 = 0
    sum2 = 0
    for item in range(begin, end + 1):
        if item % 2 == 0:
            sum += item
            avg = (sum / 2)
    print(sum)
    print(avg)
    for item in range(begin, end + 1):
        if item % 2 :
            sum1 += item
            avg1 = (sum1 / 2)
    print(sum1)
    print(avg1)
    for item in range(begin, end + 1):
        if item % 9 == 0 :
            sum2 += item
            avg2 = (sum2 / 2)
    print(sum2)
    print(avg2)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')