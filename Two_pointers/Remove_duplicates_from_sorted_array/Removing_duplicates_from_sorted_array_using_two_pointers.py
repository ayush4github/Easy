def removing_duplicates(sorted_array):
    if len(sorted_array) == 0:
        return 0
    unique_pointer = 0
    for current_pointer in range(1, len(sorted_array)):
        if sorted_array[current_pointer] != sorted_array(unique_pointer):
            unique_pointer +=1
            sorted_array[unique_pointer] = sorted_array[current_pointer]
    return unique_pointer +1
array = list(map(int, input("Enter elements of array separated by space: ").split()))
removing_duplicates(sorted(array))
print("Final array is: ", removing_duplicates)