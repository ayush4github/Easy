arr1 = list(map(int, input("Enter elements of array1 separated by space: ").split()))
arr2 = list(map(int, input("Enter elements of array2 separated by space: ").split()))
if len(arr1)!=len(arr2):
    print("Arrays are NOT equal")
else:
    freq ={}
    for element in arr1:
        freq[element]=freq.get(element, 0)+1
    for element in arr2:
        if element not in freq:
            print("Arrays are NOT equal")
            exit()
        freq[element] =freq[element]-1
    for value in freq.values():
        if value != 0:
            print("Arrays are NOT equal")
            exit()
    print("Arrays are equal")