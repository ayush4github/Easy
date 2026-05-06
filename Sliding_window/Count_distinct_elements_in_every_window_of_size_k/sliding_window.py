def count_distinct_in_window(array, k):
    result = []
    frequency_map = {}
    for i in range(k):
        element = array[i]
        frequency_map[element]=frequency_map.get(element, 0)+1
    result.append(len(frequency_map))
    for right_pointer in range(k, len(array)):
        new_element = array[right_pointer]
        frequency_map[new_element]=frequency_map.get(new_element, 0)+1
        old_element = array[right_pointer-k]
        frequency_map[old_element]-=1
        if frequency_map[old_element]==0:
            del frequency_map[old_element]
        result.append(len(frequency_map))
    return result
n = int(input("Enter number of elements in array: "))
array=[]
for x in range(n):
    element = int(input("Enter element of array: "))
    array.append(element)
k = int(input("Enter window size: "))
result = count_distinct_in_window(array, k)
print("Result is: ", result)