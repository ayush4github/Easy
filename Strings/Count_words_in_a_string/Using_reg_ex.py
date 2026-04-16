import re
String = input("Enter your string: ")
words = re.findall(r"\b\w+\b", String)
print("Number of words: ", len(words))