try:
    sum = 0
    for item in range (100 , 999 + 1):
        n1= item/100
        n2=(item/10)%10
        n3=item % 10
    if n1 == n2 == n3:
        sum += 1
    print(sum)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
