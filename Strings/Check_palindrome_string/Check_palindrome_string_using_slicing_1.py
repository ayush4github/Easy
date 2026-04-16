s = input()
if len(s)>0:
    reverse = s[::-1]
    if reverse == s:
        print("String is a palindrome")
    else: 
        print("String is not a palindrome")
else:
    print("Invalid string")