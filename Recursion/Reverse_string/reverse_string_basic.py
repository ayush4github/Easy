def reverse_string(string):
    #Base condition
    if len(string) ==0:
        return " "
    #Recursive formula
    return reverse_string(string[1:]) + string[0]
string = input("Enter string here: ")
result = reverse_string(string)
print("Reversed string: ", result)