def move_zeroes(arr):
    write_pointer = 0
    for current_pointer in range(len(arr)):
        if arr[current_pointer] != 0:
            arr[write_pointer]=arr[current_pointer]
            write_pointer +=1
    for index in range(write_pointer, len(arr)):
        arr[index] =0
    return arr
array = list(map(int, input("Enter elements of array separated by spaces: ").split()))
result_array = move_zeroes(array)
print("Result array is: ", result_array)