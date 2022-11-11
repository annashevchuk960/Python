try:
    month = int(input("Day="))
    if month <= 0:
        raise Exception('month can not be <= 0 ')
    if 12 < month:
        raise Exception('month can not be more than 12')
    if  month == 1:
        print("Січень")
    elif month == 2:
        print("Лютий")
    elif month == 3:
        print("Березень")
    elif month == 4:
        print("Квітень")
    elif month == 5:
        print("Травень")
    elif month == 6:
        print("Червень")
    elif month == 7:
        print("Липень")
    elif  month == 8:
        print("Серпень")
    elif month == 9:
        print("Вересень")
    elif month == 10:
        print("Жовтень")
    elif month == 11:
        print("Листопад")
    elif month == 12:
        print("Грудень")
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')