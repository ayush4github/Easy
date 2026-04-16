String = input()
result = {
    "Vowels" : 0,
    "Consonants" : 0,
    "Digits" : 0,
    "Spaces" : 0
}
for char in String:
    if char.lower() in "aeiou":
        result["Vowels"] += 1
    elif char.isalpha():
        result["Consonants"] +=1
    elif char.isdigit():
        result["Digits"] +=1
    elif char == " ":
        result["Spaces"] +=1
print(result)