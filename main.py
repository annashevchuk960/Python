try:
    count1 = 0
    count2 = 0
    for a in range(100, 9999):
        n1 = (a // 1000)
        n2 = (a // 100) % 10
        n3 = (a % 10) // 10
        n4 = a % 10
        if a <= 1000:
            (n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4)
            count1 += 1
        if a >= 1000:
            (n1 != n2 and n1 != n3 and n1 != n4 and n2 != n3 and n2 != n4 and n3 != n4)
            count2 += 1
    print(count1+count2)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
