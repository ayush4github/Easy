from collections import Counter
String = input("Enter your string: ")
freq = Counter(String)
for ch, count in freq.items():
    print(f"{ch}: {count}")