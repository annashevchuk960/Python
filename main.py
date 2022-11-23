try:
    number = int(input("Number="))
    if number <= 0:
        raise Exception('number can not be <= 0 ')
    if number > 100:
        raise Exception('number can not be > 100 ')
    if  number % 3 == 0 and number % 5==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz ")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')