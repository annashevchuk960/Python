try:
    length = int(input('length->'))
    sign = (input('sign->'))
    for item in range(1,length + 1):
     print  (sign,end="\t")
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')