String = input("Enter your string: ")
freq = {}
for ch in String:
    if ch != " ":
        freq[ch] = freq.get(ch, 0)+1
for ch in freq:
    print(f"{ch}: {freq[ch]}")