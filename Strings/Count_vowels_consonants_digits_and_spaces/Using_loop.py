String = input()
vowels = 0
consonants = 0
digits = 0
digits = 0
spaces = 0
for char in String:
    if char.lower() in "aeiou":
        vowels = vowels + 1
    elif char.isalpha():
        consonants = consonants + 1
    elif char.isdigit():
        digits = digits + 1
    elif char == " ":
        spaces = spaces + 1
print("Vowels", vowels)
print("Consonants", consonants)
print("Digits", digits)
print("Spaces", spaces)