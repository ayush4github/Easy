arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
result = set()
set1 = set(arr1)
for element in arr2:
    if element in set1:
        result.add(element)
print(list(result))