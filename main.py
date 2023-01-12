string = input("Рядок ")
print(len([i for i in string if i.isdigit()]))
print(len([i for i in string if i.isalpha()]))