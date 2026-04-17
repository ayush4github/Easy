def merge_sorted_arrays(arr1, arr2):
    pointer1=0
    pointer2=0
    result=[]
    while pointer1<len(arr1) and pointer2<len(arr2):
        if arr1[pointer1]<=arr2[pointer2]:
            result.append(arr1[pointer1])
            pointer1+=1
        else:
            result.append(arr2[pointer2])
            pointer2+=1
    while pointer1<len(arr1):
        result.append(arr1[pointer1])
        pointer1+=1
    while pointer2<len(arr2):
        result.append(arr2[pointer2])
        pointer2+=1
    return result
arr1= list(map(int, input("Enter elements of array 1 separated by space: ").split()))
arr2 = list(map(int, input("Enter elements of array 2 separated by space: ").split()))
Merged_Array = merge_sorted_arrays(arr1, arr2)
print("Merged array: ", result)