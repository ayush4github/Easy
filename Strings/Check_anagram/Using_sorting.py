String1 = input("Enter your first string here: ")
String2 =input("Enter your second string here: ")
if  sorted(String1.lower()) == sorted(String2.lower()):
    print("Anagram")
else:
    print("Not anagram")