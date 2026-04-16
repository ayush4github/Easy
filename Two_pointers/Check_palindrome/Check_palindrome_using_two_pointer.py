def is_palindrome(input_string):
    left = 0
    right = len(input_string)-1
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left = left +1
        right = right-1
    return True
input_string = input("Enter string here: ")
if is_palindrome(input_string):
    print("Palindrome")
else:
    print("Not palindrome")