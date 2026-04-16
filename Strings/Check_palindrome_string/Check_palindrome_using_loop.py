s = input()
reverse = ""
for char in s:
    reverse = char + reverse
if reverse == s:
    print("String is a palindrome")
else:
    print("String is not a palindrome")