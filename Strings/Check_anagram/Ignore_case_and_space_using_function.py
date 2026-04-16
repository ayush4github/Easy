from collections import Counter
def normalize(String):
    return String.replace(" ", "").lower()
String1 = input("Enter your first string here: ")
String2 = input("Enter your second string here: ")
if len(String1)!=len(String2):
    print("Anagram not possible")
else:
    if Counter(normalize(String1)) == Counter(normalize(String2)):
        print("Anagram")
    else:
        print("Not anagram")