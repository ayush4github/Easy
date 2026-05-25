def reverse_array(array, left_index, right_index):
    if left_index >= right_index:
        return
    #Swap Elements
    array[left_index], array[right_index] = array[right_index], array[left_index]
    #Recursive call
    reverse_array(array, left_index +1, right_index-1)
#Input
array = list(map(int, input("Enter elements of array separated by space: ").split()))
reverse_array(array, 0, len(array)-1)
#Output
print("Reversed array: ", array)