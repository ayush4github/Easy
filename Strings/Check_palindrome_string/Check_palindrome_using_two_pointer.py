s = input()
left = 0
right = len(s)-1
is_Palindrome = "String is a palindrome"
while left < right:
    if s[left] != s[right]:
        is_Palindrome = "String is not a palindrome"
        break
    left = left +1
    right = right -1
print(is_Palindrome)