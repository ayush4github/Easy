arr1= list(map(int, input("Enter elements of array1 separated by space: ").split()))
arr2 = list(map(int, input("Enter elements of array2 separated by space: ").split()))
if arr1 == arr2:
    print("Arrays are equal")
else:
    print("Arrays are NOT equal")