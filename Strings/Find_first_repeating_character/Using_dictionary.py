String = input("Enter your string here: ")
freq = {}
for char in String:
    freq[char] = freq.get(char, 0)+1
result = None
for char in String:
    if freq[char]>1:
        result = char
        break
if result:
    print("First repeating character is: ", result)
else:
    print("No repeating character found")