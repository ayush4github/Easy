arr = list(map(int, input().split()))
count_zeros = arr.count(0)
for i in range(count_zeros):
    arr[i] = 0
for i in range(count_zeros, len(arr)):
    arr[i] = 1
print(arr)