String = input("Enter your string here: ")
freq = {}
for ch in String:
    freq[ch] = freq.get(ch, 0)+1
for ch in String:
    if freq[ch] ==1:
        result = ch
        break
if result:
    print("First non-repeating character is: ", result)
else:
    print("No first non-repeating character found.")