Array = list(map(int, input().split()))
freq= {}
for element in Array:
    if element in freq:
        freq[element] = freq[element]+1
    else:
        freq[element] =1
for key in freq:
    print(f"{key}: {freq[key]}")