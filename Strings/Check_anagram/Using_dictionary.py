String1 = input("Enter your first string here: ")
String2 = input("Enter your second string here: ")
if len(String1) != len(String2):
    print("Anagram not possible")
else:
    freq = {}
    for char in String1.lower():
        freq[char] = freq.get(char, 0)+1
    for char in String2.lower():
        if char not in freq:
            result = "Not anagram"
        else:
            result = "Anagram"
    print(result)