def removing_elements(array, target):
    left_pointer = 0
    right_pointer = len(array)-1
    while left_pointer <=right_pointer:
        if array[left_pointer]==target:
            array[left_pointer]=array[right_pointer]
            right_pointer-=1
        else:
            left_pointer+=1
    return left_pointer
array = list(map(int, input("Enter elements of array separated by space: ")))
target = int(input("Enter element to remove: "))
new_length = removing_elements(array, target)
print("New length: ", new_length)
print("Modified array: ", array[:new_length])