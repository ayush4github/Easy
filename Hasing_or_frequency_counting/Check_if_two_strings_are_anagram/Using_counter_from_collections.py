from collections import Counter
String1 = input("Enter first string: ").lower().replace(" ", "")
String2 = input("Enter second string: ").lower().replace(" ", "")
if Counter(String1) == Counter(String2):
    print("Anagram")
else:
    print("Not anagram")