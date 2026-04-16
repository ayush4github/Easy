from collections import Counter
String = input("Enter your string here: ")
freq = Counter(String)
for ch in String:
    if freq[ch] ==1:
        print("First non-repeating character: ", ch)
        break
else:
        print("No non-repeating character found")