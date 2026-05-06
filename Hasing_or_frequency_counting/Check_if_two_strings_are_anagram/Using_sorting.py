String1 = input("Enter first string: ").lower().replace(" ", "")
String2 = input("Enter second string: ").lower().replace(" " ,"")
if sorted(String1) == sorted(String2):
    print("Is anagram")
else:
    print("Is not anagram")