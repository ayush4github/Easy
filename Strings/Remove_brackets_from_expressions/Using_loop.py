Expression = input("Enter your string here: ")
result = ""
for char in Expression:
    if char not in "()":
        result = result + char
print(result)