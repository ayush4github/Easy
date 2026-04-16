Expression = input("Enter your string here: ")
result = "".join([char for char in Expression if char not in "()"])
print(result)