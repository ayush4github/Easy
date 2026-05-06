String1 = input("Enter first string: ").lower().replace(" ", "")
String2 = input("Enter second :string: ").lower().replace(" ", "")
if len(String1) != len(String2):
    print("Anagram not possible")
else:
    freq ={}
    for char in String1:
        freq[char] = freq.get(char, 0)+1
    for char in String2:
        if char not in freq:
            print("Not anagram")
            exit()
        freq[char] =freq[char]-1
    for value in freq.values():
        if value !=0:
            print("Not anagram")
            exit()
    print("Anagram")