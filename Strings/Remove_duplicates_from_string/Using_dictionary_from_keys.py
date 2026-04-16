String = input("Enter your string here: ")
result = "".join(dict.fromkeys(String))
print(result)