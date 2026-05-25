def is_palindrome(string, left_index, right_index):
    if left_index >= right_index:
        return True
    if string[left_index] != string[right_index]:
        return False
    return is_palindrome(
        string,
        left_index +1,
        right_index -1
    )
string = input("Enter a string: ")
result = is_palindrome(string, 0, len(string)-1)
if result:
    print("Palindrome")
else:
    print("Not Palindrome")