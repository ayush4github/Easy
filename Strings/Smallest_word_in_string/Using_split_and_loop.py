words = input("Enter your string here: ").split()
smallest = words[0]
for word in words:
    if len(word)<len(smallest):
        smallest = word
print("Smallest word in the strings is: ", smallest)