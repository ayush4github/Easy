String = input("Enter your string here: ")
seen = set()
for char in String:
    if char in seen:
        result = char
    seen.add(char)
if result:
    print("First repeating character is: ", result)
else:
    print("No repeating character found")