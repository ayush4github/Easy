def is_Anagram(string1, string2):
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    if sorted_string1 == sorted_string2:
        return "Anagram"
    else:
        return "Not anagram"
string1 = input("Enter string1 here: ")
string2 = input("Enter string2 here: ")
result = is_Anagram(string1, string2)
print("Both strings are: ", result)
    