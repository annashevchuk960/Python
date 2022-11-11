try:
    day = int(input("Day="))
    if day <= 0:
        raise Exception('day can not be <= 0 ')
    if 7 < day:
        raise Exception('day can not be more than 7')
    if  day == 1:
        print("Понеділок")
    elif day == 2:
        print("Вівторок")
    elif day == 3:
        print("Середа")
    elif day == 4:
        print("Четвер")
    elif day == 5:
        print("П'ятниця")
    elif day == 6:
        print("Субота")
    elif day == 7:
        print("Неділя")
    else:
        print('Command not found!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')