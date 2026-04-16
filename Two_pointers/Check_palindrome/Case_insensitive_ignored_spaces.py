def is_Palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    left = 0
    right = len(cleaned_string)-1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left = left +1
        right = right-1
    return True
text = input("Enter your string here: ")
if is_Palindrome(text):
    print("Palindrome")
else:
    print("Not palindrome")