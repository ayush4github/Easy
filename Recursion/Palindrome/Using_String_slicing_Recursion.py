def is_palindrome(string):
    #Base case
    if len(string) <= 1:
        return True
    #First and last character mismatch
    if string[0] != string[-1]:
        return False
    #Recursion call
    return is_palindrome(string[1:-1])
#Input
string = input("Enter a string: ")
#Output
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not palindrome")