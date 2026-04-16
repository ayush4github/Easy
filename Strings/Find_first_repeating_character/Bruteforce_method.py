String = input("Enter your string here: ")
for i in range(len(String)):
    for j in range(i+1, len(String)):
        if String[i] == String[j]:
            print("First repeating character: ", String[i])
            break
    else:
        continue
    break
else:
    print("No repeating character found")