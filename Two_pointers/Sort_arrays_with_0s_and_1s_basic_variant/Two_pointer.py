def sort_0s_1s(array):
    left_pointer = 0
    right_pointer=len(array)-1
    while left_pointer<right_pointer:
        if array[left_pointer] ==0:
            left_pointer +=1
        elif array[right_pointer]==1:
            right_pointer-=1
        else:
            array[left_pointer], array[right_pointer]=array[right_pointer], array[left_pointer]
            left_pointer+=1
            right_pointer-=1
    return array
n = int(input("Enter number of elements of array: "))
array=[]
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
Modified_array = sort_0s_1s(array)
print("Modified array: ", Modified_array)