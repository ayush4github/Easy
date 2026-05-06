arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
freq = {}
result = {}
for element in arr:
    freq[element] = freq.get(element, 0)+1
for q in queries:
    result[q] = freq.get(q, 0)
print(result)