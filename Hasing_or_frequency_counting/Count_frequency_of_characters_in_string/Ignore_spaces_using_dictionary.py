String = input("Enter a string: ")
freq={}
for char in String:
    if char != " ":
        freq[char]=freq.get(char, 0)+1
for key in freq:
    print(f"{key}:{freq[key]}")