String = input("Enter your string here: ")
seen = set()
result = ""
for char in String:
    if char.lower() not in seen:
        seen.add(char.lower())
        result = result + char
print(result)