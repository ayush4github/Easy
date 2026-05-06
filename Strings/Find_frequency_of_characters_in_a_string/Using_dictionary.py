String = input("Enter your string here: ")
freq = {}
for char in String:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
print(freq)