import re
String = input()
result = re.sub(r"\s+", "", String)
print("String without whitespaces: ", result)