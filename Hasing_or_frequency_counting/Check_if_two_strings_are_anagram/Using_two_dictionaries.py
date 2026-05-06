String1 =input("Enter first string: ").lower().replace(" ", "")
String2 = input("Enter second string: ").lower().replace(" ", "")
if len(String1)!=len(String2):
    print("Not an anagram")
else:
    freq1={}
    freq2={}
    for char1 in String1:
        freq1[char1] = freq1.get(char1, 0)+1
    for char2 in String2:
        freq2[char2] = freq2.get(char2, 0)+1
    if freq1!=freq2:
        print("Not anagram")
    else:
        print("Anagram")