String = input()
result = ""
for ch in String:
    if ch.islower():
        result = result + ch.upper()
    elif ch.isupper():
        result = result + ch.lower()
    else:
        result = result + ch
print(result) 