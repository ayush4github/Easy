from collections import Counter
String = input("Enter a string: ")
freq=Counter(String)
for key in freq:
    print(f"{key}: {freq[key]}")