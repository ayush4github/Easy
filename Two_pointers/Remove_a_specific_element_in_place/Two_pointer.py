def remove_element(array, target):
    write_pointer=0
    for current_pointer in range(len(array)):
        if array[current_pointer]!=target:
            array[current_pointer]=array[current_pointer]
            write_pointer +=1
    return write_pointer
array = list(map(int, input("Enter elementd of array separated by space: ").split()))
target = int(input("Enter target element to remove: "))
new_length = remove_element(array, target)
print("New length: ", new_length)
print("Modified array: ", array[:new_length])
