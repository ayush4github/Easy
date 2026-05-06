String = input("Enter your string here: ")
if all(char.isdigit() for char in String):
    print("String contains only digits")
else:
    print("String does NOT contains only digits")