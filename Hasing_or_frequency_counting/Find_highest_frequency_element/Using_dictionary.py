try:
    n = int(input())
    Array = []
    for i in range(n):
        element = int(input())
        Array.append(element)
except:
    print("Invalid input")
freq={}
for char in Array:
    freq[char] = freq.get(char, 0)+1
max_element = Array[0]
max_count = freq[max_element]
for key in freq:
    if freq[key]>max_count:
        max_count=freq[key]
        max_element=key
print(max_element)