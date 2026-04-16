String = input("Enter your string here: ")
try:
    int(String)
    print("String contains only digits")
except ValueError:
    print("String does NOT contains only digits")