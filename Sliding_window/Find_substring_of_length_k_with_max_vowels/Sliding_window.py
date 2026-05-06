def max_vowels_substring(s, k):
    vowels=set("aeiouAEIOU")
    window_vowel_count=0
    max_vowels=0
    for right_pointer in range(len(s)):
        if s[right_pointer] in vowels:
            window_vowel_count+=1
        if right_pointer>=k:
            if s[right_pointer-k] in vowels:
                window_vowel_count-=1
        if right_pointer >=k-1:
            max_vowels=max(max_vowels, window_vowel_count)
    return max_vowels
n = int(input("Enter number of elements in string: "))
s=[]
for x in range(n):
    element = int(input("Enter element of string: "))
    s.append(element)
k = int(input("Enter window size: "))