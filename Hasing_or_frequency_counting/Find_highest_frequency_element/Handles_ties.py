arr = []

try:
    n = int(input())
    for i in range(n):
        element = int(input())
        arr.append(element)
except:
    print("Invalid input")
    exit()

if not arr:
    print("Empty array")
    exit()

freq = {}
for element in arr:
    freq[element] = freq.get(element, 0) + 1

result = max(freq, key=freq.get)