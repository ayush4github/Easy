arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
result = list(set(arr1).intersection(set(arr2)))
print("Intersection: ", result)