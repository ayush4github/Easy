String = input("Enter your string here: ")
for char in String:
    if not char.isdigit():
        result = "String does NOT contains only digits"
    else:
        result = "String contains only digits"
print(result)