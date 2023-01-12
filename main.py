string = input("Рядок ")
letcount = 0
numcount = 0
for symbol in string:
    if symbol.isalpha():
        letcount += 1
    if symbol.isdigit():
        numcount += 1
print('Літери', letcount )
print('Цифри', numcount)