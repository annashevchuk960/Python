number = int(input("number="))
if 0 <= number < 6:
    print ("Good Night")
elif 6 <= number < 13:
    print("Good Morning")
elif 13 <= number < 17:
    print("Good Day")
elif 17 <= number < 0 :
    print("Good Evening")
else
    print('Command not found!')