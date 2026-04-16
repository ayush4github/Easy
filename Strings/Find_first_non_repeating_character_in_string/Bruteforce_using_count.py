String = input("Enter your string: ")
for char in String:
    if String.count(char) ==1:
        print("First non-repeating character is: ", char)
        break
    else:
        print("No non-repeating character found")