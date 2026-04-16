arr1 = list(map(int, input("Enter elements of array 1 separated by space here: ").split()))
arr2 = list(map(int, input("Enter elements of array 2 separated by space here: ").split()))
if sorted(arr1) == sorted(arr2):
    print("Arrays are equal")
else:
    print("Arrays are NOT equal")