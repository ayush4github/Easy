Array = list(map(int, input("Enter your array here: ").split()))
freq={}
for element in Array:
    freq[element] = freq.get(element, 0)+1
for key in sorted(freq):
    print(f"{key}: {freq[key]}")