from collections import Counter
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
freq = {}
result = {}
freq = Counter(arr)
for q in queries:
    result[q] = freq.get(q, 0)
print(result)