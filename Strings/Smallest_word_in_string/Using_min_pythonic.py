String = input("Enter your string here: ")
smallest = min(String.split(), key= len)
print("Smallest word in the string is: ", smallest)