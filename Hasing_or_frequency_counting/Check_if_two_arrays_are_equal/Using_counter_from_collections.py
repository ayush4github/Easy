from collections import Counter
arr1 = list(map(int, input("Enter elements of arr1 separated by spaces: ").split()))
arr2 = list(map(int, input("Enter elements of arr2 separated by spaces: ").split()))
if Counter(arr1) == Counter(arr2):
    print("Arrays are equal")
else:
    print("Arrays are NOT equal")