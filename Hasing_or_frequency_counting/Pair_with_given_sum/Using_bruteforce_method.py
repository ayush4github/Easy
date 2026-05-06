arr = list(map(int, input("Enter elements separated by space: ").split()))
target = int(input("Enter targeted sum: "))
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] +arr[j] == target:
            pairs.append((arr[i], arr[j]))
if pairs:
    print("Pairs: ", pairs)
else:
    print("No pair found")