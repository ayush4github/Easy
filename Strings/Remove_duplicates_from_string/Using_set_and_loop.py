String = input("Enter your string here: ")
seen = set()
result = ""
for char in String:
    if char not in seen:
        seen.add(char)
        result = result+char
print(result)