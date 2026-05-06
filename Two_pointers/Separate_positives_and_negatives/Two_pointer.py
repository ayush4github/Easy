def separate_positives_and_negatives(array):
    left_pointer = 0
    right_pointer = len(array)-1
    while left_pointer < right_pointer:
        while left_pointer < right_pointer and array[left_pointer]<0:
            left_pointer+=1
        while left_pointer < right_pointer and array[right_pointer]>=0:
            right_pointer-=1
        if left_pointer<right_pointer:
            array[left_pointer], array[right_pointer]=array[right_pointer], array[left_pointer]
    return array
array = list(map(int, input("Enter elements of array separated by space: ").split()))
result = separate_positives_and_negatives(array)
print("Modified array: ", result)