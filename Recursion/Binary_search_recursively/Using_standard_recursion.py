def binary_search(array, left_index, right_index, target):
    #Base case
    if left_index > right_index:
        return -1
    #Middle index
    middle_index = (left_index + right_index) // 2
    #Target found
    if array[middle_index] == target:
        return middle_index
    #Search left half
    if target < array[middle_index]:
        return binary_search(array, left_index, middle_index-1, target)
    #Search right half
    if target > array[middle_index]:
        return binary_search(array, middle_index+1, right_index, target)
#Input array
array = list(map(int, input("Enter elements of array separated by space: ").split()))
#Target
target = int(input("Enter target element: "))
#Function call
result = binary_search(array, 0, len(array)-1, target)
#Output
if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")