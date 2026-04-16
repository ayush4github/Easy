Array=list(map(int, input().split()))
freq={}
for element in Array:
    freq[element] = freq.get(element, 0)+1
    min_count = min(freq.values())
    for key in freq:
        if freq[key] == min_count:
            result = key
print(result)