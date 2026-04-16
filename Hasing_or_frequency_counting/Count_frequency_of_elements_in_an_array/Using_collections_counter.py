from collections import Counter
Array = list(map(int, input("Enter your string here: ").split()))
freq= Counter(Array)
for key in freq:
    print(f"{key}: {freq[key]}")