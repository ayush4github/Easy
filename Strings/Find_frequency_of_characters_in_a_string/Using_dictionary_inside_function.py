class Solutions:
    def char_frequency(self, text):
        freq={}
        for char in text:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] =1
        return freq
text = input("Enter your string: ")
obj = Solutions()
result = obj.char_frequency(text)
for key in result:
    print(f"{key}: {result[key]}")